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


def clear_popups():
    buttons = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div/div[2]/button')
    if len(buttons) > 0:
        print('Trying to clear popup.')
        button = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/button')
        print('Pressing', button.get_attribute('innerHTML'))
        time.sleep(1)
        button.click()
        print('popup cleared')
    else:
        print('No popup to clear.')


def add_student():
    add_more_students = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[2]/a')
    print('Clicking add more students...')
    add_more_students.click()
    print('Ready to add students')


try:
    print('Loading website...')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userName')))
    print('Website loaded. Logging in...')
    login()
    print('Logged in. Waiting for the page to refresh...')
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/h1')))
    print('Page refreshed. Waiting for any pop to appear...')
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/button')))
    print('Popup appeared. Clearing popup...')
    time.sleep(5)
    clear_popups()
    time.sleep(5)
    print('Popup appeared. Clearing popup...')
    clear_popups()
    add_student()

except:
    print('Error: something went wrong')
finally:
    print('Turning Off...')
    time.sleep(3000)
    driver.quit()




