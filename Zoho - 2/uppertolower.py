def UpperToLower(val):
  store = ""
  for i in val:
    if ord(i)>=ord("A") and ord(i)<=ord("Z"):
      store += chr(ord(i)+32)
    else:
      store += i
  return(store)

val = input("Enter a string: ")
print(UpperToLower(val))