#  A = And B = or c = Xor
# Input: 1B1C0A1

val = input("Enter the string: ")
ans = int(val[0])
for i in range(2,len(val),2):
  k = val[i-1]
  
  if k == 'A':
    ans = ans and int(val[i])
  elif k == 'B':
    ans = ans or int(val[i])
  elif k == 'C':
    ans = ans ^ int(val[i])
print(ans)