import os
from dotenv import load_dotenv
import requests

load_dotenv()
SERVICE_KEY = os.environ.get('SERVICE_KEY')

# url = "https://apis.data.go.kr/B551011/KorService1/searchFestival1?&numOfRows=100&pageNo=1&MobileOS=ETC&MobileApp=TestApp&_type=json&eventStartDate=20240101&serviceKey=" + SERVICE_KEY

url2 = "https://apis.data.go.kr/B551011/KorService1/searchFestival1?&numOfRows=100&pageNo=1&MobileOS=ETC&MobileApp=TestApp&_type=json&eventStartDate=20240101&serviceKey=jZR3uJFxdc0NscrCZcAtbbRDBKO3wPtamGJW%2BEVrgnX4%2BlgmaUk8MCAjAdE0q3ypRZfObKESyJ0ZNfN1cdn%2Fwg%3D%3D"
requestData = requests.get(url2)
jsonData = None

if requestData.status_code == 200 :
    jsonData = requestData.json()

    print(jsonData)