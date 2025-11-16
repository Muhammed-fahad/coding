def NoOfLeapDays(year):
    return year//4 - year//100 + year//400

def InWhichYear(n):
    low = 1
    high = 10000   # enough upper limit

    while low <= high:
        mid = (low + high) // 2
        count = NoOfLeapDays(mid)

        if count < n:
            low = mid + 1
        else:
            high = mid - 1

    return low


year = int(input("Enter the year: "))
print("Number of leap years till", year, "is:", NoOfLeapDays(year))

n = int(input("Enter N (which leap year you want): "))
print(f"The {n}th leap year comes in:", InWhichYear(n))
