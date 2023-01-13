import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = r"C:\Users\User\Downloads\Compressed\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=path)

driver.get(website)
all_matches_button =  driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')
time.sleep(5)

matches = driver.find_elements(By.TAG_NAME, "tr")
date = []
home_team = []
score = []
away_team =[ ]
for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

driver.quit()

df = pd.DataFrame({'date':date, 'home_team':home_team,'score':score, 'away_team':away_team})
df.to_csv('C:\\Users\\User\\OneDrive\\Documents\\football_data_spain.csv',index=False)
print(df)

