from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from datetime import datetime
import time 
import pandas as pd

def initialize_columns():
    return pd.DataFrame(columns=['진행 매체', '브랜드명', '브랜드URL', '이벤트정보', '상품 유형', '라이브 일자', '라이브 URL'])

def initialize_page(current_date, given_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--ignore-certificate-errors')

    formatted_date = current_date.strftime("%Y%m%d")
    url = given_url + formatted_date

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

    previous = driver.execute_script("return document.body.scrollHeight")
    interval = 5

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(interval)
        current = driver.execute_script("return document.body.scrollHeight")

        if previous == current:
            break

        previous = current

    return driver
