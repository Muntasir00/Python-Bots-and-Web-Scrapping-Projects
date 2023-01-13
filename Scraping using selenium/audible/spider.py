from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()



options.add_experimental_option("detach", True)
path = r"C:\Users\User\Downloads\Compressed\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=path)

web = 'https://www.audible.com/search'
driver.get(web)
driver.maximize_window()

container = driver.find_element(By.CLASS_NAME,"adbl-impression-container")
products = container.find_elements(By.XPATH,'./li')

for product in products:
    product.find_element(By.XPATH, '//h3[contains(@class,"bc-heading")]').text
    product.find_element(By.XPATH, '//li[contains(@class,"authorLabel")]').text