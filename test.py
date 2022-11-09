from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://www.exploretock.com/hayato/")

print(driver.title)
