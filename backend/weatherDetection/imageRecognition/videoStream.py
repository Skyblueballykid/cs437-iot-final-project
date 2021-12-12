from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# url = "http://68.225.115.149:8443/"

url = "http://apple.com"
driver.get(url)
driver.save_screenshot("./test.jpg")