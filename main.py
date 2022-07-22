from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

website = 'https://schooleducation.southpunjab.gov.pk/SPeTS/'

driver = webdriver.Chrome()
driver.get(website)


def login():
    school_id = '31120050'
    school_pw = 'MC8319936'
    username = driver.find_element(By.ID, 'userName')
    password = driver.find_element(By.ID, 'userPassword')
    sign_in_button = driver.find_element(By.ID, 'btnSignin')
    username.clear()
    password.clear()
    username.send_keys(school_id)
    password.send_keys(school_pw)
    sign_in_button.click()


def add_student():
    dashboard = 'https://schooleducation.southpunjab.gov.pk/SPeTS/dashboard.php'
    print(dashboard)
    print('Ready to add students')


try:
    print('loading website')
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userName')))
    print('website loaded. logging in')
    login()
    print('logged in. waiting for the page to refresh')
    logged_in = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
        'body > div.bootbox.modal.fade.bootbox-alert.show > div > div > div.modal-footer > button')))
    print('page refreshed...')
    print(logged_in)
    logged_in.click()
    add_student()

finally:
    time.sleep(3000)
    driver.quit()




