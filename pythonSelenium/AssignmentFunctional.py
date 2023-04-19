import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
#time.sleep(4)
itemNames = driver.find_elements(By.XPATH, "//div[@class='product']//h4[@class='product-name']")
for itemName in itemNames:
    actualList.append(itemName.text)
print(actualList)
assert expectedList == actualList

results = driver.find_elements(By.XPATH, "//div[@class='product']//button[text()='ADD TO CART']")
print(len(results))
for result in results:
    result.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Code applied ..!']")))
promotext = driver.find_element(By.XPATH, "//span[text()='Code applied ..!']").text
print(promotext)
assert promotext == "Code applied ..!"

addedItemsTotals = driver.find_elements(By.CSS_SELECTOR, ".cartTable tbody tr td:nth-child(5) p")
sum = 0
for addedItemsTotal in addedItemsTotals:
    sum = sum + int(addedItemsTotal.text)
print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount

totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert totalAmount > totalAfterDiscount

driver.close()
