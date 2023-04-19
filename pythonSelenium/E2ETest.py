import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(@href, 'shop')] - Xpath
# a[href*='shop'] - CSS
driver.find_element(By.XPATH, "//a[text()='Shop']").click()

products = driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
for product in products:
    if product.find_element(By.CSS_SELECTOR, ".card-title a").text == "Blackberry": # Getting Balckberry text
        product.find_element(By.CSS_SELECTOR, ".btn").click() # After getting Blackberry text then click on Add
        break

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

driver.find_element(By.ID, "country").send_keys("Ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

successAlert = driver.find_element(By.CSS_SELECTOR, ".alert-success").text
assert "Success! Thank you!" in successAlert
driver.close()

