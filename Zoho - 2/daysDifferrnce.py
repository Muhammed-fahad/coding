def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def findDays(year, months, day):
    year -= 1
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_before = year * 365 + year // 4 + year // 400 - year // 100 + day + sum(month[:months - 1])

    if months > 2:
        if(is_leap(year+1)):
            days_before += 1
    return days_before

year1 = list(map(int , input("Enter year, month, day (space separated): ").split()))
year2 = list(map(int , input("Enter year, month, day (space separated): ").split()))  

daysIny1 = findDays(year1[0], year1[1], year1[2])
print(daysIny1)
daysIny2 = findDays(year2[0], year2[1], year2[2])

print(abs(daysIny2 - daysIny1))
