from common.web_imports import *
from common.common_functions import get_next_date, initialize_dates
from bs4 import BeautifulSoup
from datetime import datetime

today, current_date, end_date = initialize_dates(3, 7)
df = initialize_columns()

while current_date <= end_date:
    given_url = 'https://shoppinglive.naver.com/calendar?d='
    driver = initialize_page(current_date, given_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all('div', attrs={'class': 'VideoBoxWrapper_wrap_Usbk7 VerticalCardList_item_YPN88 CalendarListContent_item_hSue8 BroadcastSideCard_tablet_GUyN4 BroadcastSideCard_has_left_video_time_L739e'})
    
    try:
        for i, item in enumerate(items):

            category = '라이브특가'
            sub_category = '네이버쇼핑라이브'
            brand = item.find('span', class_='ChannelProfile_name_jT9wN').text
            brand_href = item.find('a', class_='VideoBoxLinkWrapper_wrap_GLkZS BroadcastSideCard_link_profile_11zQW')['href']
            brand_url = 'https://shoppinglive.naver.com/' + brand_href
            live_url = item.find('a')['href']  
            
            live_time_string = item.find('time')['datetime'].split('.')
            splited_time_obj = live_time_string[0]
            live_time = datetime.strptime(splited_time_obj, "%Y-%m-%dT%ggH:%M:%S").strftime("%m/%d %H시 %M분")

            df = pd.concat([df, pd.DataFrame([[sub_category, brand, brand_url, category, '상품유형 확인', live_time, live_url]], columns=df.columns)], ignore_index=True)

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

    driver.quit()
    current_date = get_next_date(current_date)

address = "C:\\work\\"
df_sorted = df.sort_values(by='라이브 일자', ascending=True)
df_sorted.to_excel(excel_writer=address + today.strftime("%Y%m%d") + '_네이버.xlsx', index=False)