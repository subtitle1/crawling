from common.mobile_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(1, 5)
df = initialize_columns()

while current_date <= end_date :
    formatted_date = current_date.strftime("%Y%m%d")
    url = 'https://shoppinglive.kakao.com/api/v1/live-calendar?date=' + formatted_date

    requestData = requests.get(url)
    jsonData = None

    if requestData.status_code == 200 :
        jsonData = requestData.json()
        productList = jsonData.get("contents")

        try: 
            category = '라이브특가정보'
            sub_category = '카카오쇼핑라이브'

            for item in productList:
                print(item)
                product_category = item['categoryName']
                live_url = 'https://shoppinglive.kakao.com/live/' + item['liveContentId']

                live_time = item['liveStartAt']
                # image_url = item['imageUrl']
                
                df = pd.concat([df, pd.DataFrame([[category, sub_category, 'brand', '', category, product_category, live_time, live_url]], columns=df.columns)], ignore_index=True)
                # df = pd.concat([df, pd.DataFrame([[sub_category, brand, brand_url, category, '상품유형 확인', live_time, live_url]], columns=df.columns)], ignore_index=True)

        except Exception:
            pass

    current_date = get_next_date(current_date)

address = "C:\\work\\"
df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_kakao.xlsx')
