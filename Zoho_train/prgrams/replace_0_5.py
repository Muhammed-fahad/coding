number = 10230430
val = 0
k = 1

while(number > 0):
  digit = number % 10
  if digit == 0:
    digit = 5
  val += digit * k
  k*=10
  number = number//10

print(val)