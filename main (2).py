from datetime import date
import calendar
event = input("Enter event title:")
year = int(input("Enter year(YYYY): "))
month = int(input("Enter month(1-12): "))
day = int(input("Enter day(1-31): "))
date = date(year,month,day)
print("Event: ", event.upper())
print("Date: ", date.strftime("%B %d, %Y"))
print("Year: ", year)
print("Month: ", calendar.month_name[month])
print("Day: ", day)
print("Weekday: ", date.strftime("%A"))


