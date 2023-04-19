import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
# time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='product']//button[text()='ADD TO CART']")
print(len(results))

for result in results:
    result.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
promotext = driver.find_element(By.XPATH, "//span[text()='Code applied ..!']").text
print(promotext)
assert promotext == "Code applied ..!"

addedItemsTotals = driver.find_elements(By.CSS_SELECTOR, ".cartTable tbody tr td:nth-child(5) p")
sum = 0
for addedItemsTotal in addedItemsTotals:
    sum = sum + int(addedItemsTotal.text)
print(sum)

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert sum == int(totalAmount)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()



driver.close()



