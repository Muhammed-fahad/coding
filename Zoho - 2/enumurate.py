a = ["Fahad", "Sheik" , "Sayira" , "Nadeem"]
for i,j in enumerate(a):
  print(i+1,".",j)

for i , j in zip(range(1,10+1) , range(10,0,-1)):
  print(i,j)
  
for k,l in zip(a , a[::-1]):
  print(k ," " ,l)