import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        #time.sleep(2)
        assert checkbox.is_selected()
        break


radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")

print(len(radiobuttons))

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio3":
        radiobutton.click()
        #time.sleep(2)
        assert radiobutton.is_selected()
        break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

driver.close()
