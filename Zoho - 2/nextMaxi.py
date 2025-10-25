def nextMaxi(val1):
  for i in range(0,len(val1)-1):
    maxi = max(val1[i+1:len(val1)])
    val1[i] = maxi
  val1[-1] = -1
  return (val1)


val = list(map(int, input("Enter a numbers: ").split()))
print(nextMaxi(val))


# new = [-1]*len(val)
# new_val = -1
# for i in range(len(val)-1,-1,-1):
#   temp = val[i]
#   new[i] = new_val
#   new_val = max(temp,new_val)
# print(new)