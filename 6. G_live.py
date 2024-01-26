from common.mobile_imports import *
from common.common_functions import get_next_date, initialize_dates

url = 'https://m.gmarket.co.kr/n/live/_next/data/bMXsOgO3o7Wlc3Y8T3dKE/n/live/schedule.json'
requestData = requests.get(url)
jsonData = None

if requestData.status_code == 200 :
    jsonData = requestData.json()
    productList = jsonData['pageProps']['initialStates']['schedule']['liveCatalogs']

    print(productList)

    # liveURL = landingUrl
    # imageUrl, broadcastTitle, brand_logo = seller['logoImage'], brand = seller['name']
    # start_live_time = broadcastStartDate, live_end_time = broadcastEndDate