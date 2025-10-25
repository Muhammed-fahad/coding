val1 = input("Enter a number: ")
val2 = input("Enter a number: ")
v1 = 0
v2 = 0
for i in val1:
  v1*= 10
  v1+= ord(i)-ord('0')

for i in val2:
  v2*= 10
  v2+= ord(i)-ord('0')

print(v1*v2)