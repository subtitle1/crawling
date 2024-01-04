import requests
import pandas as pd

def initialize_columns():
    return pd.DataFrame(columns=['카테고리', '서브카테고리', '브랜드명', '브랜드URL', '이벤트정보', '상품유형', '이벤트 기간', '라이브 URL'])