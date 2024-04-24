import calendar

def month_to_days(month_name, year):
    month_number = list(calendar.month_name).index(month_name)
    return calendar.monthrange(year, month_number)[1]

month_name = "April"
year = 2024
print(f"The number of days in {month_name} {year} is {month_to_days(month_name, year)}")