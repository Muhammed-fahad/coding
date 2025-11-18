s = "([]{()})"
l = []
matching = {')':'(' , ']':'[' , '}':'{'}

for i in s:
  if i in "({[":
    l.append(i)
    
  elif i in ")}]":
    if not l or l[-1] != matching[i]:
      print("Not valid")
      break
    l.pop()
else:
  if not l:
    print("Valid")
  else:
    print("Not Valid")