import calendar
year=int(input("enter year: "))
month=int(input("enter month: "))
day=int(input("enter date : "))
dayy= calendar.weekday(year,month,day)
print("day: {}-{}".format(dayy,calendar.day_name[dayy]))
print()