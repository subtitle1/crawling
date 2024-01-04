from common.web_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(1, 6)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')

df = initialize_columns()

while current_date <= end_date:
    formatted_date = current_date.strftime("%Y%m%d")
    url = 'https://shoppinglive.naver.com/calendar?d=' + formatted_date

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

    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all('div', attrs={'class': 'VideoBoxWrapper_wrap_Usbk7 lico-home__sc-e630726c-0 fTvbot BroadcastSideCard_card_tBFMO'})

    try:
        for i, item in enumerate(items):
            category = '라이브특가정보'
            sub_category = '네이버쇼핑라이브'
            brand = item.find('span', class_='ChannelProfile_name_jT9wN').text
            live_url = item.find('a')['href']  
            
            live_time_string = item.find('time')['datetime'].split('.')
            splited_time_obj = live_time_string[0]
            live_time = datetime.strptime(splited_time_obj, "%Y-%m-%dT%H:%M:%S").strftime("%m/%d %H시 %M분")

            df = pd.concat([df, pd.DataFrame([[category, sub_category, brand, '', category, '', live_time, live_url]], columns=df.columns)], ignore_index=True)

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

    driver.quit()
    current_date = get_next_date(current_date)

# address = "C:\\Users\\Mars\\Desktop\\work\\"
address = "C:\\work\\"
df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_네이버.xlsx')