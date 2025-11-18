# convert 12hr formate into 24hr
hour = input("Enter hour in 12hr with am/pm: ").split(":")
hour[0] , hour[1] = int(hour[0]) , int(hour[1])

if hour[2] == "am":
  if(hour[0] == 12):
    hour[0] = 0
  print(hour[0],":",hour[1])
  
else:
  if hour[0] != 12:
    hour[0]+= 12
  print({hour[0]},":",hour[1]) 