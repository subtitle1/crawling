from common.mobile_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(3, 8)
df = initialize_columns()

while current_date <= current_date :
    formatted_date = current_date.strftime("%Y%m%d")
    url = 'https://www.hmall.com/api/hf/dp/v1/etv-mng/tv-list-pc?mainDispSeq=2&brodType=etv&date=' + formatted_date

    requestData = requests.get(url)
    jsonData = None

    if requestData.status_code == 200 :
        jsonData = requestData.json()
        productList = jsonData["respData"]["brodList"]

        category = "라이브특가정보"
        sub_category = "Hmall 홈쇼핑"
        # 브랜드명(brodSbtl -> 틀릴 수도 있음), price, 상품코드(slitmCd), live_url, 
        # 정상가(original_price) / sellPrc, 할인가격(discounted_price) / hmallBbprc, 
        live_url = "https://www.hmall.com/pd/pda/itemPtc?slitmCd="
        print(productList)