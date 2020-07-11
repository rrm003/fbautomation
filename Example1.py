from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()                     #creates chrome instance 
driver.get("http://facebook.com")            #The driver.get method will navigate to a page given by the URL


def login() : 
    ID = driver.find_element_by_id("email")
    PASSWORD = driver.find_element_by_name("pass")
    LOGIN_BTN = driver.find_element_by_id("u_0_b")
    ID.send_keys("rammankar003@gmail.com")
    PASSWORD.send_keys("Gohome@003")
    LOGIN_BTN.click()

def post() : 
    
    text = "Script Generated text. Ignore!!"
    text_space = driver.find_element(By.XPATH,'.//*[@name="xhpc_message"]')
    text_space.send_keys(text)
    time.sleep(5)
    btn_xpath = "//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']"
    post_btn = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, btn_xpath)))
    post_btn.click()
        
'''def logout() : 
    btn = driver.find_element_by_id("logoutMenu")
    btn.click()
'''    
time.sleep(10)    
login()
time.sleep(10)
post()
#logout()
