def pali(value):
  return value == value[::-1]


val = str(input("Enter a string: "))
val = val.lower()
print(pali(val))