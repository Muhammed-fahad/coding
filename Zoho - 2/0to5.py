# 120003270
# 125553275

# 12308
# 12358 

n = int(input("Enter a number: "))
ans = 0
multi = 1

while(n>0):
  k = n%10
  if(k == 0):
    ans+= 5*multi
  else:
    ans+= k*multi
  n//=10
  multi*=10
print(ans)
