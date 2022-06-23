from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Eliot Aldersson\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(2)

driver.get('https://unicen.edu.bo/')

WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.NAME,
                                           'wdform_2_element6'))) \
        .send_keys('Eliot Aldersson')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                           'wdform_6_element6'))) \
    .send_keys('Medicina')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                           'wdform_7_element6'))) \
    .send_keys('+591 76221133')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                           'wdform_3_element6'))) \
    .send_keys('Eliot.Aldersson05.09@gmail.com')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.NAME,
                                           'wdform_14_element6'))) \
    .send_keys('Cochabamba')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.NAME, 'wdform_15_element6'.replace(
                                               ' ', '.')))) \
    .send_keys('Bolivia')

WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CLASS_NAME, 'button-submit'.replace(
                                               ' ', '.')))) \
    .click()

time.sleep(20)
driver.quit()