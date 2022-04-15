from sys import executable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from predict import all_in_one
link = 'https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fconsole%2Fhome%3Ffromtb%3Dtrue%26hashArgs%3D%2523%26isauthcode%3Dtrue%26region%3Dus-east-1%26skipRegion%3Dtrue%26state%3DhashArgsFromTB_us-east-1_902eea85f37a990d&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&forceMobileApp=0&code_challenge=BgNqgYhaBs8AM_RUu-VnsUgs8mb_g8N8krN7iJO5hPI&code_challenge_method=SHA-256'
chromrdriver = "C:/Users/HP/Downloads/chromedriver_win32 (1)/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get(link)
driver.find_element_by_id("resolving_input").send_keys("muradaliyev2229@gmail.com")
driver.find_element_by_id("next_button").click()
time.sleep(2)
image = driver.find_element_by_xpath("//*[@id='captcha_image']")
slc = image.get_attribute("src")
print(all_in_one(slc))

