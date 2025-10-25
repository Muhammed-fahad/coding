# Testcase 1:
# Input: Java1234
# Output: Javb1234 (Remove the second ‘a’ as it is duplicated)
# Testcase 2:
# Input: Python1223:
# Output: Python1234 

def replace(s):
  seen = set()
  store = ""
  
  for char in s:
    char = char
    while char in seen:
        char = chr(ord(char)+1)  
    store+=char
    seen.add(char)
  return store
    
val = input("Enter a String: ")
print(replace(val))
