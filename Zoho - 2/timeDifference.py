# we wanted to find the time difference , date and time is given 
# 12/43/am
# 21/12/25

# 12/43/pm
# 22/12/25

def differenceindays(days):
    day = int(days[0])
    mon = int(days[1])
    year = int(days[2]) - 1 

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    totaldays = year * 365 + day + sum(months[:mon - 1]) + year // 4 + year // 400 - year // 100

    if mon > 2:
        if (year + 1) % 4 == 0 and ((year + 1) % 100 != 0 or (year + 1) % 400 == 0):
            totaldays += 1
    return totaldays

def time_convertion(time):
    hour, minu, presidence = int(time[0]), int(time[1]), time[2].lower()
    if presidence == "am" and hour == 12:
        hour = 0
    elif presidence == "pm" and hour != 12:
        hour += 12
    return hour * 60 + minu

time1 = input("Enter time 1 (hh/mm/am or pm): ").split("/")
date1 = input("Enter date 1 (dd/mm/yy): ").split("/")

time2 = input("Enter time 2 (hh/mm/am or pm): ").split("/")
date2 = input("Enter date 2 (dd/mm/yy): ").split("/")

total_minutes1 = differenceindays(date1) * 24 * 60 + time_convertion(time1)
total_minutes2 = differenceindays(date2) * 24 * 60 + time_convertion(time2)

diff = abs(total_minutes2 - total_minutes1)
hours = diff // 60
minutes = diff % 60

print(f"Time difference is {hours:02} hrs and {minutes:02} min")