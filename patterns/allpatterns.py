n = int(input("Enter a number: "))
for i in range(1,n+1):
  a = 1
  for j in range(1,2*n):
    if(i+j >= n+1 and j-i <= n-1):
      if(j>=n):
        print(a,end=" ")
        a-=1
      else:
        print(a,end=" ")
        a+=1
    else:
      print(" ",end=" ")
  print()

print("---------------------------------")

for i in range(1,n+1):
  a = 5
  for j in range(1,2*n):
    if(i+j >= n+1 and j-i <= n-1):
      if(j>=n):
        print(a,end=" ")
        a+=1
      else:
        print(a,end=" ")
        a-=1
    else:
      print(" ",end=" ")
  print()
  

print("---------------------------------")

for i in range(1,n+1):
  a = i
  for j in range(1,2*n):
    if(i+j>=n+1 and j-i<=n-1):
      if(j<n):
        print(a,end=" ")
        a+=1
      else:
        print(a,end=" ")
        a-=1
    else:
      print(" ",end=" ")
  print()
  
print("---------------------------------")

for i in range(1,2*n):
  if(i<=n):
    a=i
  else:
    a = 2*n-i
  for j in range(1,n+1):
    if(i>=j):
      if(a>0):
        print(a,end=" ")
        a-=1
    else:
      print(" ",end=" ")
  print()
  
print("---------------------------------")