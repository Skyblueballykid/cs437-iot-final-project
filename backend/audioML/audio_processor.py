"""
    simple_audio.py

    This programs collects audio data from a two channel USB microphone
    and runs a TensorFlow Lite interpreter on the yamnet audio classification model. 

"""

from scipy.io import wavfile
from scipy import signal
import numpy as np
import argparse 
import pyaudio
import wave
import time
import librosa
import zipfile
from tflite_runtime.interpreter import Interpreter



VERBOSE_DEBUG = False
# reference: https://electronut.in/audio-recongnition-ml/
# get pyaudio input device
def getInputDevice(p):
    index = 3
    nDevices = p.get_device_count()
    print('Found %d devices:' % nDevices)
    for i in range(nDevices):
        deviceInfo = p.get_device_info_by_index(i)
        #print(deviceInfo)
        devName = deviceInfo['name']
        print(devName)
        # choose input device from list
        if not index:
            if 'input' in devName.lower():
                index = i
    # print out chosen device
    if index is not None:
        devName = p.get_device_info_by_index(index)["name"]
        #print("Input device chosen: %s" % devName)
    return index

def get_live_input():
    CHUNK = 4096
    FORMAT = pyaudio.paInt32
    CHANNELS = 2
    RATE = 16000 
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "test.wav"
    NFRAMES = int((RATE * RECORD_SECONDS) / CHUNK)

    # initialize pyaudio
    p = pyaudio.PyAudio()
    getInputDevice(p)

    print('opening stream...')
    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = CHUNK,
                    input_device_index = 1)

    #discard first 1 second
    for i in range(0, NFRAMES):
        data = stream.read(CHUNK, exception_on_overflow = False)

    try:
        while True:
            print("Listening...")

            frames = []
            for i in range(0, NFRAMES):
                data = stream.read(CHUNK, exception_on_overflow = False)
                frames.append(data)

            # process data
            buffer = b''.join(frames)
            audio_data = np.frombuffer(buffer, dtype=np.int32)
            nbytes = CHUNK * NFRAMES 
            # reshape for input 
            audio_data = audio_data.reshape((nbytes, 2))
            # run inference on audio data 
            return run_inference(audio_data)
    except KeyboardInterrupt:
        print("exiting...")
           
    stream.stop_stream()
    stream.close()
    p.terminate()

def process_audio_data(waveform):
    """Process audio input.

    This function takes in raw audio data and adjusts to 15600 length
    to match yamnet parameters

    """

    if VERBOSE_DEBUG:
        print("waveform:", waveform.shape, waveform.dtype, type(waveform))
        print(waveform[:5])

    # if stereo, pick the left channel
    if len(waveform.shape) == 2:
        print("Stereo detected. Picking one channel.")
        waveform = waveform.T[1]
    else: 
        waveform = waveform 

    if VERBOSE_DEBUG:
        print("After scaling:")
        print("waveform:", waveform.shape, waveform.dtype, type(waveform))
        print(waveform[:5])

    # normalise audio
    wabs = np.abs(waveform)
    wmax = np.max(wabs)
    waveform = waveform / wmax

    PTP = np.ptp(waveform)
    #print("peak-to-peak: %.4f. Adjust as needed." % (PTP,))

    # return None if too silent 
    if PTP < 0.5:
        return []

    if VERBOSE_DEBUG:
        print("After normalisation:")
        print("waveform:", waveform.shape, waveform.dtype, type(waveform))
        print(waveform[:5])

    # scale and center
    waveform = 2.0*(waveform - np.min(waveform))/PTP - 1

    # extract 15600 len (.975 seconds) of data   
    max_index = np.argmax(waveform)  
    start_index = max(0, max_index-7800)
    end_index = min(max_index+7800, waveform.shape[0])
    waveform = waveform[start_index:end_index]

    # Padding for files with less than 15600 samples
    if VERBOSE_DEBUG:
        print("After padding:")

    waveform_padded = np.zeros((15600,))
    waveform_padded[:waveform.shape[0]] = waveform

    if VERBOSE_DEBUG:
        print("waveform_padded:", waveform_padded.shape, waveform_padded.dtype, type(waveform_padded))
        print(waveform_padded[:5])

    return waveform_padded


def run_inference(waveform):
    #source: https://tfhub.dev/google/lite-model/yamnet/classification/tflite/1
    # get spectrogram data 
    spectrogram = process_audio_data(waveform)

    if not len(spectrogram):
        #disp.show_txt(0, 0, "Silent. Skip...", True)
        print("Too silent. Skipping...")
        #time.sleep(1)
        return 


    if VERBOSE_DEBUG:
        print("spectrogram1: %s, %s, %s" % (type(spectrogram), spectrogram.dtype, spectrogram.shape))

    # load TF Lite model
    interpreter = Interpreter('yamnet_model.tflite')
    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    waveform_input_index = input_details[0]['index']
    output_details = interpreter.get_output_details()
    scores_output_index = output_details[0]['index']


    input_shape = input_details[0]['shape']
    waveform = spectrogram.astype(np.float32)

    interpreter.resize_tensor_input(waveform_input_index, [waveform.size], strict=True)
    interpreter.allocate_tensors()
    interpreter.set_tensor(waveform_input_index, waveform)

    print("running inference...")
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    yvals = output_data[0]
    labels_file = zipfile.ZipFile('yamnet_model.tflite').open('yamnet_label_list.txt')
    
    labels = [l.decode('utf-8').strip() for l in labels_file.readlines()]
    scores = interpreter.get_tensor(scores_output_index)
    top_class_index = scores.argmax()


    if VERBOSE_DEBUG:
        print(output_data[0])

    weather_sounds = ['Rain', 'Raindrop', 'Rain on surface', 'Thunderstorm', 'Thunder', 'Wind', 'Rustling Leaves']

    animal_sounds = ['Bird', 'Bird vocalization, bird call, bird song', 'Chirp, tweet', 'Dog', 'Bark', 'Yip']

    if labels[top_class_index] in (weather_sounds or animal_sounds):
        print(labels[top_class_index])
        return labels[top_class_index]
    else:
        return " "

def process_wav(wav_file):
    sampling_rate = 16000
    # get audio data 
    original_rate, waveform = wavfile.read(wav_file)

    # resample data
    number_of_samples = round(len(waveform) * float(sampling_rate) / original_rate)
    waveform = signal.resample(waveform, number_of_samples)
    # run inference
    return run_inference(waveform)

def main():

    # create parser
    descStr = """
    This program recognizes audio using the yamnet tflite model.
    """
    parser = argparse.ArgumentParser(description=descStr)
    # add a mutually exclusive group of arguments
    group = parser.add_mutually_exclusive_group()

    # add expected arguments
    group .add_argument('--input', dest='wavfile_name', required=False)
    
    # parse args
    args = parser.parse_args()

    # test WAV file
    if args.wavfile_name:
        process_wav(args.wavfile_name)
    else:
        get_live_input()

    print("done.")

# main method
if __name__ == '__main__':
    main()
