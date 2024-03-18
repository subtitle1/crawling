from common.mobile_imports import *
from common.common_functions import get_next_date, initialize_dates

today, current_date, end_date = initialize_dates(1, 5)
df = initialize_columns()

bd_date = current_date.strftime("%Y%m%d")
formatted_date = current_date.strftime("%Y-%m-%d")
url = 'https://www.lotteimall.com/main/scheduleLive.lotte?bdDate=' + bd_date + '&date=' + formatted_date

requestData = requests.get(url)
jsonData = None

if requestData.status_code == 200 :
    jsonData = requestData.json()

    print(jsonData)

