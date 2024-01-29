from common.mobile_imports import *
from common.common_functions import get_next_date, initialize_dates
from datetime import datetime

today, current_date, end_date = initialize_dates(3, 8)
df = initialize_columns(date_format=True)

while current_date <= end_date :
    formatted_date = current_date.strftime("%Y%m%d")

    url = 'https://www.hmall.com/api/hf/dp/v1/etv-mng/tv-list-pc?mainDispSeq=2&brodType=etv&date=' + formatted_date
    requestData = requests.get(url)
    jsonData = None

    if requestData.status_code == 200 :
        jsonData = requestData.json()
        productList = jsonData["respData"]["brodList"]

        category = "라이브특가정보"
        sub_category = "Hmall 홈쇼핑"

        try:
            for item in productList:

                input_format = "%Y%m%d%H%M%S"
                output_format = "%m/%d %H시 %M분"

                start_live_time_str = item['brodStrtDtmParam']
                end_live_time_str = item['brodEndDtmParam']

                start_live_time = datetime.strptime(start_live_time_str, input_format).strftime(output_format)
                end_live_time = datetime.strptime(end_live_time_str, input_format).strftime(output_format)
                
                brand = item['brodSbtl']
                title = item['slitmNm']
                original_price = item['sellPrc']
                discounted_price = item['bbprc']
                live_url = "https://www.hmall.com/pd/pda/itemPtc?slitmCd=" + item['slitmCd']

                df = pd.concat([df, pd.DataFrame([[category, sub_category, title, brand, original_price, discounted_price, category, '', start_live_time, end_live_time, live_url, '']], columns=df.columns)], ignore_index=True)

        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            pass

        current_date = get_next_date(current_date)

address = "C:\\work\\"
df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_H몰.xlsx')
