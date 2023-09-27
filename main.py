import pandas as pd


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


custom_options = Options()
custom_options.add_argument("--start-maximized")
path_driver = Service('chromedriver.exe')
driver = webdriver.Chrome(service=path_driver, options=custom_options)
link = "https://www.flashscore.com.ua/"
driver.get(link)
class_name = 'event__match.event__match--twoLine'
driver_m = driver.find_elements(By.CLASS_NAME, class_name)
matches_results = []
for element in driver_m:
    matches_results.append(element.text.splitlines())
columns = [
    'status',
    'team 1',
    'team 2',
    'goals 1',
    'goals 2',
    'first time 1',
    'first time 2',
    'sl 1',
    'sl 2'
]
result = pd.DataFrame(matches_results, columns=columns)
drop_cols = ['sl 1', 'sl 2']
result = result.drop(drop_cols, axis=1)
result = result.loc[result['status'] == 'Завершен']
result.to_excel('football_result.xlsx', index=False)
