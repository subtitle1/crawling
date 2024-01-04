from common.web_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(1, 5)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-certificate-errors')

df = initialize_columns()

while current_date <= end_date:
    formatted_date = current_date.strftime("%Y%m%d")
    url = 'https://shoppinglive.kakao.com/calendar?t_src=shopping_live&t_ch=home&t_obj=header_calendar&date=' + formatted_date

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
    items = soup.find_all('ul', attrs={'class': 'list_liveguide'})

    try:
        for i, item in enumerate(items):
            category = '라이브특가정보'
            sub_category = '카카오쇼핑라이브'
            live_items = item.select('ul.list_liveguide > li')

            for live_item in live_items:
                
                live_time = current_date.strftime("%m/%d ") + live_item.select_one('.txt_time').text.strip()
                product_category = live_item.select_one('a.link_prd')['data-tiara-category']
                live_url = 'https://shoppinglive.kakao.com' + live_item.select_one('a.link_prd')['href']

                df = pd.concat([df, pd.DataFrame([[category, sub_category, 'brand', '', category, product_category, live_time, live_url]], columns=df.columns)], ignore_index=True)

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

    driver.quit()
    current_date = get_next_date(current_date)

address = "C:\\work\\"
df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_카카오.xlsx')