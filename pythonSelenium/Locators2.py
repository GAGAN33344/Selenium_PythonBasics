from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input"). send_keys("Gagan") # using by tag name Xpath
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input"). send_keys("Gagan") # using by tag name Css
driver.find_element(By.XPATH, "//button[text() = 'Save New Password']").click() # Xpath using text

driver.close()
