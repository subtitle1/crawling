import requests
import pandas as pd

def initialize_columns(date_format=False):
    # 홈쇼핑의 경우
    if date_format:
        return pd.DataFrame(columns=['카테고리', '서브카테고리', '광고명', '브랜드명', '기존 가격', '할인 가격', '이벤트정보', '상품유형', '시작 시간', '종료 시간', '라이브 URL', '브랜드 LOGO', '이미지 URL'])
    # 라이브의 경우
    else:
        return pd.DataFrame(columns=['카테고리', '서브카테고리', '브랜드명', '브랜드URL', '이벤트정보', '상품유형', '이벤트 기간', '라이브 URL'])
    

# 예제 사용
# df1 = initialize_columns()
# df2 = initialize_columns(date_format=True)