from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# ID, Name, ClassName, TagName, LinkText, PartialLinkText, CSSSelector, xPath
# //tagname[@attribute='value'] XPATH
# tagname[attribute='value'] CSSSelector, #id, .className,
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Gaganpreet S Mann") # Name Field
driver.find_element(By.NAME, "email").send_keys("gaganmann@gmail.com") # Email Field
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password") # Password Field
driver.find_element(By.ID, "exampleCheck1").click() # click Icon
# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click() # Click Radiobutton Student
driver.find_element(By.XPATH, "//input[@value='Submit']").click() # Submit Button
successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successMessage)
assert "Success!" in successMessage
driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("HelloAgain")
driver.close()