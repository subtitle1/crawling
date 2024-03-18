from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd

# next: 0
# query: 블루밍데이즈 or 신제품
# size: 10
# sortType: POPULAR
# statusType: READY
# slSessionId: 37211862-066c-44d4-b8e3-bea782a9aed8

# query = input("검색어 입력: ")
url = 'https://shoppinglive.naver.com/search/lives?query=블루밍데이즈'

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

# previous = driver.execute_script("return document.body.scrollHeight")
# interval = 1

# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#     time.sleep(interval)
#     current = driver.execute_script("return document.body.scrollHeight")

#     if previous == current:
#         break

#     previous = current

soup = BeautifulSoup(driver.page_source, "html.parser")
items = soup.find_all('div', attrs={'class': 'TitleMoreLinkSection_wrap_mp+Z0 TitleMoreLinkSection_has_last_child_padding_GHBry TitleMoreLinkSection_has_border_eE00I TitleMoreLinkSection_tablet_k1mYW SearchNextLive_wrap_YbMRI SearchNextLive_has_border_+8FeV'})

print(items)

# while current_date <= end_date:
#     given_url = 'https://shoppinglive.naver.com/calendar?d='
#     driver = initialize_page(current_date, given_url)

#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     items = soup.find_all('div', attrs={'class': 'VideoBoxWrapper_wrap_Usbk7 VerticalCardList_item_YPN88 CalendarListContent_item_hSue8 BroadcastSideCard_tablet_GUyN4 BroadcastSideCard_has_left_video_time_L739e'})

#     try:
#         for i, item in enumerate(items):
#             category = '라이브특가'
#             sub_category = '네이버쇼핑라이브'
#             brand = item.find('span', class_='ChannelProfile_name_jT9wN').text
#             live_url = item.find('a')['href']  
            
#             live_time_string = item.find('time')['datetime'].split('.')
#             splited_time_obj = live_time_string[0]
#             live_time = datetime.strptime(splited_time_obj, "%Y-%m-%dT%H:%M:%S").strftime("%m/%d %H시 %M분")

#             df = pd.concat([df, pd.DataFrame([[category, sub_category, brand, '', category, '', live_time, live_url]], columns=df.columns)], ignore_index=True)

#     except Exception as e:
#         print(f"오류가 발생했습니다: {e}")

#     driver.quit()
#     current_date = get_next_date(current_date)

# # address = "C:\\Users\\Mars\\Desktop\\work\\"
# address = "C:\\work\\"
# df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_네이버.xlsx')