# 1+4+7=12
# 2+5+8=15
# 3+6+9=18

# op = 12+15+18=45

arr = [1,2,3,4,5,6,7,8,9]
gap = 3
value = []
for i in range(len(arr)//gap):
  ans = 0
  for j in range(i,len(arr),gap):
    ans+=arr[j]
  value.append(ans)
print(value)