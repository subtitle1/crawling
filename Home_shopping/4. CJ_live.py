# web
from common.web_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(3, 8)
df = initialize_columns()

while current_date <= current_date:
    given_url = 'https://display.cjonstyle.com/p/homeTab/main?BSCCN1=SA_NV_B_PC_7&BSCPN=CJmall&BSPRG=NVBRNO&hmtabMenuId=002409#bdDt%3A'
    driver = initialize_page(current_date, given_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all('div', attrs={'class': 'schedule_prod'})

    try:
        for item in enumerate(items):
            category = '라이브특가정보'
            sub_category = 'CJ쇼핑라이브'
            # print(item)

            state_bar_element = soup.find('h4', class_='state_bar')
            program_time = state_bar_element.find('span', class_='pgmDtm').text.strip()
            chedule_prod_ul = state_bar_element.find_next('ul', class_='list_schedule_prod')
            schedule_prod_ul = state_bar_element.find_next('ul', class_='list_schedule_prod')
            li_elements = schedule_prod_ul.find_all('li')

            for li_element in li_elements:
                product_name = li_element.find('span', spcid='HOME____live__subitem-001__').text.strip()
                price_range = li_element.find('em', class_='num').text.strip()
                print(f"Product: {product_name}, Price Range: {price_range}")
#             brand = item.find('span', class_='ChannelProfile_name_jT9wN').text
#             live_url = item.find('a')['href']  
            
#             live_time_string = item.find('time')['datetime'].split('.')
#             splited_time_obj = live_time_string[0]
#             live_time = datetime.strptime(splited_time_obj, "%Y-%m-%dT%H:%M:%S").strftime("%m/%d %H시 %M분")

#             df = pd.concat([df, pd.DataFrame([[category, sub_category, brand, '', category, '', live_time, live_url]], columns=df.columns)], ignore_index=True)

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

#         driver.quit()
#         current_date = get_next_date(current_date)

# address = "C:\\work\\"
# df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_네이버.xlsx')