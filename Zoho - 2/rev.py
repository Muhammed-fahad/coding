# "input: 
# Rohit Sharma Virat Kohli KL Rahul 
# Output: 
# luhaR ilhoK amrahS Rohit Virat KL
# INPUT 2: 
# Rohit Sharma Virat Kohli KL Rahul Dhoni
# inohD LK tariV tihoR Sharma Kohli Rahul"


val = input("Enter a String: ")
a = val.split(" ")[::-1]
dummy =""
ls1 = []
i = 1

for i in range(len(a)):
  if (i%2 == 0):
    dummy += (a[i][::-1]) + " "
    i+=1
    
  else:
    ls1.append(a[i])
    i+=1
ls1 = ls1[::-1]
for i in ls1:
  dummy += i+" "

print(dummy)