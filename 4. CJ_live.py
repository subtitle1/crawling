# web
from common.web_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(3, 8)
df = initialize_columns()

while current_date <= end_date:
    given_url = 'https://display.cjonstyle.com/p/homeTab/main?BSCCN1=SA_NV_B_PC_7&BSCPN=CJmall&BSPRG=NVBRNO&hmtabMenuId=002409#bdDt%3A'
    driver = initialize_page(current_date, given_url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all('div', attrs={'class': 'schedule_prod'})

    print(items)