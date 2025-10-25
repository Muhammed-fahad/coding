def NoOfLeapDays(year):
  return year//4 + year//400 - year//100

year = int(input("Enter the year: "))
print(NoOfLeapDays(year))