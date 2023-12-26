from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd

query = input("검색어 입력: ")
url = "https://search.shopping.naver.com/search/all?query=" + query

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

previous = driver.execute_script("return document.body.scrollHeight")
interval = 1

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    current = driver.execute_script("return document.body.scrollHeight")

    if previous == current:
        break

    previous = current

soup = BeautifulSoup(driver.page_source, "html.parser")
items = soup.find_all('div', attrs={'class': 'product_item__MDtDF'})

# 엑셀 셀 너비 설정, 컬럼 지정
pd.set_option('display.max.colwidth', 100)
df = pd.DataFrame(columns=['순번', '제품명', '가격', 'URL'])

try:
    for i, item in enumerate(items):
        idx = i + 1
        title = item.find('div', attrs={'class': 'product_title__Mmw2K'}).text
        price = item.find('span', attrs={'class': 'price_num__S2p_v'}).text
        url = item.find('a')['href']

        df.loc[i] = [idx, title, price, url]

except Exception:
    pass

now = time
address = "C:\\work\\"
df.to_excel(excel_writer = address + query + '.xlsx')