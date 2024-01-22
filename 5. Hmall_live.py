from common.mobile_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(3, 8)
df = initialize_columns()

while current_date <= end_date :
    formatted_date = current_date.strftime("%Y%m%d")
    url = 'https://www.hmall.com/api/hf/dp/v1/etv-mng/tv-list-pc?mainDispSeq=2&brodType=etv&date=' + formatted_date

    requestData = requests.get(url)
    jsonData = None

    # https://www.hmall.com/api/hf/dp/v1/etv-mng/tv-list-pc?mainDispSeq=2&brodType=etv&date=20240111
    if requestData.status_code == 200 :
        jsonData = requestData.json()
        productList = jsonData["respData"]["liveBrodList"]

        category = "라이브특가정보"
        sub_category = "Hmall 홈쇼핑"

        try:
            for item in productList:
                title = item['slitmNm']
                start_live_time_obj = item['brodStrtDtmParam']
                end_live_time_obj = item['brodEndDtmParam']

                start_live_time = start_live_time_obj.datetime.strptime(start_live_time_obj).strftime("%m/%d %H시 %M분")
                end_live_time = end_live_time_obj.datetime.strptime(start_live_time_obj).strftime("%m/%d %H시 %M분")

                brand = item['brodSbtl']
                live_url = "https://www.hmall.com/pd/pda/itemPtc?slitmCd=" + item['slitmCd']

                print(brand, live_url, start_live_time, end_live_time)
                    # subImageList
                    # df = pd.concat([df, pd.DataFrame([[category, sub_category, brand, 'brand_url', category, '', start_live_time, end_live_time, live_url]], columns=df.columns)], ignore_index=True)

        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            pass

        current_date = get_next_date(current_date)
        # 브랜드명(brodSbtl -> 틀릴 수도 있음), price, 상품코드(slitmCd), live_url, 
        # 정상가(original_price) / sellPrc, 할인가격(discounted_price) / hmallBbprc, 
        # 시작 시간: brodStrtDtmParam / 종료 시간: brodEndDtmParam
        