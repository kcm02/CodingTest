import datetime

def solution(a, b):
    Days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    day = datetime.date(2016, a, b)
    return Days[day.weekday()]