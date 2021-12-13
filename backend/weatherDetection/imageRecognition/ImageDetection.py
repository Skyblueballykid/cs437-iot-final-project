import warnings, fastai

warnings.filterwarnings("ignore")
from fastai.vision import *
from fastai.metrics import error_rate, accuracy

model_dir = "dataset/training"
test_img = "dataset/20211212-142138.jpg"

def getWeatherConditions(model_dir, test_img):
    model_inf = load_learner(model_dir)
    test_img = open_image(test_img).resize(224)
    pred_class,pred_idx,outputs = model_inf.predict(test_img)
    return pred_class, pred_idx, outputs

pred_class, pred_idx, outputs = getWeatherConditions(model_dir, test_img)
weather_condition = '%s' %pred_class
print(weather_condition)