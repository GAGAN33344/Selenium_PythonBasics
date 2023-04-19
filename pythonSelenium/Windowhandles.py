from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
childWindowText = driver.find_element(By.TAG_NAME, "h3").text
print("Child Window Text is : " + childWindowText)
assert childWindowText == "New Window"
driver.close()

driver.switch_to.window(windows[0])
parentWindowText = driver.find_element(By.TAG_NAME, "h3").text
print("Parent Window Text is : " + parentWindowText)
assert parentWindowText == "Opening a new window"

driver.close()