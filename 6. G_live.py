from common.mobile_imports import *
from datetime import datetime

df = initialize_columns(date_format=True)
today = datetime.now()

url = 'https://m.gmarket.co.kr/n/live/_next/data/bMXsOgO3o7Wlc3Y8T3dKE/n/live/schedule.json'
requestData = requests.get(url)
jsonData = None

if requestData.status_code == 200 :
    jsonData = requestData.json()
    liveCatalogs = jsonData.get('pageProps', {}).get('initialStates', {}).get('schedule', {}).get('liveCatalogs', [])

input_format = "%Y-%m-%dT%H:%M:%S"
output_format = "%m/%d %H시 %M분"

while liveCatalogs:
    category = "라이브특가정보"
    sub_category = "G live 홈쇼핑"

    try:
        for item in liveCatalogs:
            live_list = item.get('lives', [])

            for i in live_list:
                live_url = i['broadcastSeq']
                brand = i['seller']['name']
                brand_logo = i['seller']['logoImage']

                title = i['broadcastTitle']
                live_url = i['landingUrl']
                image_url = i['imageUrl']

                start_live_time_str = i['broadcastStartDate']
                end_live_time_str = i['broadcastEndDate']

                start_live_time = datetime.strptime(start_live_time_str, input_format).strftime(output_format)
                end_live_time = datetime.strptime(end_live_time_str, input_format).strftime(output_format)

                df = pd.concat([df, pd.DataFrame([[category, sub_category, title, brand, '', '', category, '', start_live_time, end_live_time, live_url, brand_logo, image_url]], columns=df.columns)], ignore_index=True)
            liveCatalogs.pop(0)
                
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        pass

address = "C:\\work\\"
df.to_excel(excel_writer = address + today.strftime("%Y%m%d") + '_G live.xlsx')
