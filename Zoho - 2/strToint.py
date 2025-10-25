num = str(input("Enter a Number : "))
val = 0
for i in num:
  val*= 10
  n = ord(i) - ord('0')
  val+= n 
print((val))


# print(ord("1"))
# print(ord("9"))
# A= ord("9")
# B= ord("0")
# print(A-B)
# print(type(A))
