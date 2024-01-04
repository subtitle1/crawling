from datetime import datetime, timedelta

def get_next_date(current_date):
    return current_date + timedelta(days=1)

def initialize_dates(A, B):
    today = datetime.now()
    current_date = today + timedelta(days=A)
    end_date = today + timedelta(days=B)
    return today, current_date, end_date