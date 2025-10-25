# from datetime import date

# def days_between_dates(d1, m1, y1, d2, m2, y2):
#     date1 = date(y1, m1, d1)
#     date2 = date(y2, m2, d2)
#     print(date2-date1)
#     return (date2 - date1).days


# d1, m1, y1 = 10, 2, 2014
# d2, m2, y2 = 10, 3, 2015

# print(days_between_dates(d1, m1, y1, d2, m2, y2))  # Output: 393


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return days_per_month[month - 1]

def days_from_start(d, m, y):
    days = d  # Start with the given day
    for year in range(1, y):  # Add all days from previous years
        days += 366 if is_leap(year) else 365
    for month in range(1, m):  # Add all days from previous months in current year
        days += days_in_month(month, y)
    return days

def days_between_dates(d1, m1, y1, d2, m2, y2):
    return abs(days_from_start(d2, m2, y2) - days_from_start(d1, m1, y1))

# Example Usage
d1, m1, y1 = list(map(int, input("Enter day and year: ").split()))  # 10, 2, 2014 
d2, m2, y2 = list(map(int, input("Enter day and year: ").split()))  # 10, 3, 2015

print(days_between_dates(d1, m1, y1, d2, m2, y2))  # Output: 393
