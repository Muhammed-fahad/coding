# You're given a number n. If write all the numbers from 1 to n in a paper, 
# we have to find the number of characters written on the paper.For example if n=13, 
# the output should be 18 if n = 101, the output should be 195


def count():
  n = input("Enter a number: ")
  length = len(n)-1
  n = int(n)
  if (n<=9):
    return n
  else:
    return 9+((n-9)*2)+(length)

print(count())