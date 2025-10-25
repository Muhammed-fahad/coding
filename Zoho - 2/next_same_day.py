def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_same_calendar(year):
    shift = 0
    orig_leap = is_leap(year)
    y = year
    while True:
        y += 1
        shift += 2 if is_leap(y) else 1
        if shift % 7 == 0 and is_leap(y) == orig_leap:
            return y

print(next_same_calendar(2007))