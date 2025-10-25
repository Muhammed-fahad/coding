parentheses = input("Enter parentheses {[()]}: ")
arr = []

flag = True

if parentheses[0] in ")}]":
  print("parentheses are not matched")

for i in parentheses:
  if len(parentheses) % 2 != 0:
    print("parentheses are not matched")
    flag = False    
    break
  
  elif i in "{[(" :
    arr.append(i)
  
  elif i in ")]}":
    if i==')' and arr[-1] == '(':
      arr.pop()
    
    elif i==']' and arr[-1] == '[':
      arr.pop()
    
    elif i=='}' and arr[-1] == '{':
      arr.pop()

    else:
      print("parentheses are not matched")
      flag = False

if flag:
  print("parentheses are matched")