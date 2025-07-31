import time
from selenium import webdriver
from selenium.webdriver.common import options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

# browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

# time.sleep(2)

# elem = browser.find_element(By.ID, 'search')

elem_name = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, 'user-name'))
)
elem_name.send_keys('standard_user')

elem_pass = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, 'password'))
)
elem_pass.send_keys('secret_sauce')

# btn = browser.find_element(By.ID, 'login-button')
btn = browser.find_element(By.CSS_SELECTOR, '#login-button')

btn.click()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list'))
)

# time.sleep(2)

items = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')

for it in items:
    print(it.text)

browser.quit()
