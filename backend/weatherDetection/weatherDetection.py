from urllib.request import urlopen
import json

#------------WEATHER IMAGE RECOGNITION (FROM ImageDetection.py)------------
import warnings, fastai

warnings.filterwarnings("ignore")
from fastai.vision import *
from fastai.metrics import error_rate, accuracy

model_dir = "imageRecognition/dataset/training"
test_img = "imageRecognition/dataset/20211212-142138.jpg"

def getWeatherConditions(model_dir, test_img):
    model_inf = load_learner(model_dir)
    test_img = open_image(test_img).resize(224)
    pred_class,pred_idx,outputs = model_inf.predict(test_img)
    return pred_class, pred_idx, outputs

pred_class, pred_idx, outputs = getWeatherConditions(model_dir, test_img)
weather_condition = '%s' %pred_class

#------------------------------------------------------------------------

# store the URL in url as parameter for urlopen
url = "https://telemetry-dropoff.s3.us-west-2.amazonaws.com/telemetry.json"
# store the response of URL
response = urlopen(url)
# storing the JSON response from url in data
data = json.loads(response.read())[0]

weather = {}
weather["image"] = weather_condition

# Temperature Ranges
if data["temperature_fahrenheit"] <= 25:
    weather["temp"] = "frigid"
if data["temperature_fahrenheit"] <= 41:
    # weather.append("cold")
    weather["temp"] = "cold"
elif data["temperature_fahrenheit"] <= 50:
    # weather.append("chilly")
    weather["temp"] = "chilly"
elif data["temperature_fahrenheit"] <= 65:
    # weather.append("cool")
    weather["temp"] = "cool"
elif data["temperature_fahrenheit"] <= 73:
    # weather.append("room_temp")
    weather["temp"] = "room_temp"
elif data["temperature_fahrenheit"] <= 82:
    # weather.append("warm")
    weather["temp"] = "warm"
elif data["temperature_fahrenheit"] <= 90:
    # weather.append("hot")
    weather["temp"] = "hot"
elif data["temperature_fahrenheit"] <= 102:
    # weather.append("sweltering")
    weather["temp"] = "sweltering"

# Humidity Ranges
if data["humidity"] <= 20 or data["humidity"] > 60:
    # weather.append("uncomfortable") #uncomfortably_dry
    weather["humidity"] = "uncomfortable"
elif data["humidity"] <= 60:
    # weather.append("comfortable")
    weather["humidity"] = "comfortable"

# Based on Beaufort Wind Scale
# http://gyre.umeoce.maine.edu/data/gomoos/buoy/php/variable_description.php?variable=wind_2_speed
if data["wind_mph"] < 1:
    # weather.append("no_winds")
    weather["winds"] = "none"
elif data["wind_mph"] < 7:
    # weather.append("light_winds")
    weather["winds"] = "light"
elif data["wind_mph"] < 24:
    # weather.append("moderate_winds")
    weather["winds"] = "moderate"
else:
    # weather.append("strong_winds")
    weather["winds"] = "strong"

print(weather)