from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
browserSortedVeggies = []
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggieWebelements = driver.find_elements(By.XPATH, "//tbody//tr//td[1]")

for veggie in veggieWebelements:
    browserSortedVeggies.append(veggie.text)
originalBrowserSortedList = browserSortedVeggies.copy()
print(originalBrowserSortedList)

browserSortedVeggies.sort()
print(browserSortedVeggies)

assert originalBrowserSortedList == browserSortedVeggies


driver.close()
