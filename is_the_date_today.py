from datetime import datetime

def is_today(date : datetime) -> bool:
    today = datetime.now().date()
    return (date.year == today.year and date.month == today.month and date.day == today.day)