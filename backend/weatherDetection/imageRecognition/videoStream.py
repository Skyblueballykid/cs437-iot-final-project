from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime

currentDT = datetime.datetime.now()
filename = currentDT.strftime("%Y%m%d-%H%M%S")

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://68.225.115.149:8443/"
driver.get(url)
driver.save_screenshot("./training/" + filename + ".jpg")