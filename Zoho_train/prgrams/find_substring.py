s = "GreekskdmForGeeks"
find = "oma"
flage = True


for i in range(len(s) - len(find)):
  if s[i:i+len(find)] == find:
    print(i)
    flage = False
    break

if(flage):
  print("-1")