from datetime import datetime, timedelta
import requests
import pandas as pd

def get_next_date(current_date):
    return current_date + timedelta(days=1)

today = datetime.now()
current_date = today + timedelta(days=3)
end_date = today + timedelta(days=14)

df = pd.DataFrame(columns=['카테고리', '서브카테고리', '브랜드명', '브랜드URL', '이벤트정보', '상품유형', '이벤트 기간', '라이브 URL'])
# df = pd.DataFrame(columns=['카테고리', '서브카테고리', '브랜드명', '브랜드URL', '이벤트정보', '상품유형', '이벤트 기간', '라이브 URL', '이미지 URL'])

while current_date <= end_date :
    formatted_date = current_date.strftime("%Y%m%d")
    url = 'https://apis.11st.co.kr/pui/v2/page?pageId=LIVE11TIMETBLPAGE&carrSn=8276&metaCtgrNo=0&selectDate=' + formatted_date

    requestData = requests.get(url)
    jsonData = None

    if requestData.status_code == 200 :
        jsonData = requestData.json()
        productList = jsonData.get("data")[0].get("blockList")[2].get("list")

        try: 
            liveStatus = productList[0].get("liveStatusString")

            if liveStatus == "방송예정" :
                category = '라이브특가정보'
                sub_category = '11번가쇼핑라이브'

                for item in productList:
                    title = item['title']
                    live_time = item['liveScheduleDay']
                    live_url = item['liveDetailsUrl']
                    image_url = item['imageUrl']
                    
                    channel_info = item['channelInfo']
                    brand = channel_info['title']
                    brand_url = channel_info['linkUrl'] 
                    # channel_image_url = channel_info['imageUrl']

                    df = pd.concat([df, pd.DataFrame([[category, sub_category, brand, brand_url, category, '', live_time, live_url]], columns=df.columns)], ignore_index=True)
                    # df = pd.concat([df, pd.DataFrame([[category, sub_category, brand, brand_url, category, '', live_time, live_url, image_url]], columns=df.columns)], ignore_index=True)

        except Exception:
            pass

    current_date = get_next_date(current_date)

address = "C:\\work\\"
df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_11번가.xlsx')