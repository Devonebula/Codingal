from datetime import date, time, datetime

today=date.today()
now=datetime.now()
print(f"Today the date is {today} and the time is {now}")

print(today.year, today.month, today.day)