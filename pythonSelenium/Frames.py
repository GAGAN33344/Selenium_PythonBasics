from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/rahulshetty/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/")

exampleLinks = driver.find_elements(By.XPATH, "//ul//li//a")

for exampleLink in exampleLinks:
    if exampleLink.text == "Frames":
        exampleLink.click()
        break

driver.find_element(By.LINK_TEXT, "iFrame").click()

driver.switch_to.frame("mce_0_ifr")
print(driver.find_element(By.XPATH, "//body//p").text)

driver.find_element(By.XPATH, "//body//p").clear()
driver.find_element(By.XPATH, "//body//p").send_keys("Entered text in iFrame")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, ".example h3").text)

driver.close()

