from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# -- Chrome
service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/chromeDriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# -- Firefox (Not Working I don't know why)
# service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/geckoDriver/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

# -- Edge
#service_obj = Service("C:/Users/gagan/OneDrive/Desktop/BrowserDrivers/edgeDriver/msedgedriver.exe")
#driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/")
#actualTitle = "Selenium, API Testing, Software Testing & More QA Tutorials | Rahul Shetty Academy"
#expectedTitle = driver.title
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#assert(actualTitle, expectedTitle)
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()



