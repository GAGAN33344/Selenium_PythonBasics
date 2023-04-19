from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# -- Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)