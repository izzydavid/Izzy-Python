# %%
import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# %%
chromedriver_location = "/Users/davidirizarry/Downloads/chromedriver"
driver = webdriver.Chrome('/Users/davidirizarry/Downloads/chromedriver')
wrkbk = openpyxl.load_workbook('/Users/davidirizarry/Desktop/test.xlsx')
sh = wrkbk['Sheet1']
print(sh.max_row)
for c in sh['A']:
    driver.get(c.value)
    # time.sleep(1)
    print(c.value)

# %%
WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_0_2_rg"]/div[5]'
WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/header/div[2]/nav/div[2]/button[2]'
WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="endpoint"]/tp-yt-paper-item/yt-formatted-string'
WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/section/main/article/div[2]/div[2]/p/a'
WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav/ol/li[4]/a'


driver.find_element('xpath', create_new_facebook_account).click()
driver.find_element('xpath', login_instacart).click()
driver.find_element('xpath', explore_youtube).click()
driver.find_element('xpath', signup_instagram).click()
driver.find_element('xpath', signup_stack_overflow).click()
