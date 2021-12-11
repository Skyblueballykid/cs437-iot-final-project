#!/usr/bin/env python3

import time
import board
import argparse
import adafruit_sht4x
import json
import datetime


FILE_NAME = "temp-telemetry.json"
SLEEP_TIME = 1


class TempSensor:
    def __init__(self, timestamp, temperature_fahrenheit, humidity):
        self.timestamp = timestamp
        self.temperature_fahrenheit = temperature_fahrenheit
        self.humidity = humidity

    def __rep__(self):
        return self.__dict__


def write_file(json_dumped: str, file_name: str):
    with open(file_name, "w") as file_handle:
        file_handle.write(json_dumped)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    data_path = args.data_path
    i2c = board.I2C()
    sht = adafruit_sht4x.SHT4x(i2c)
    print("Found SHT4x with serial number", hex(sht.serial_number))
    sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
    print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])

    while True:
        temp_sensor = TempSensor(
            timestamp=str(datetime.datetime.now())[:16],
            temperature_fahrenheit=celsius_to_fahrenheit(sht.temperature),
            humidity=sht.relative_humidity,
        )
        print("Temperature: %0.1f f" % temp_sensor.temperature_fahrenheit)
        print("Humidity: %0.1f %%\n" % temp_sensor.humidity)
        json_dumped = json.dumps([temp_sensor.__rep__()])
        write_file(json_dumped, data_path + FILE_NAME)
        time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-path",
        type=str,
        required=False,
        help="path to write data files",
        default="/home/pi/temphumidity-data/",
    )
    args = parser.parse_args()
    main()
