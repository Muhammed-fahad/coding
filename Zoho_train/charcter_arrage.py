# Custom String Sorting

# Given two strings S and T, sort the characters of T based on the order in S. 
# Characters not in S can be placed anywhere at the end.


s = "cba"
T = "abccddmlm"

count = {}
total = []

for i in T:
  if i not in count:
    count[i] = 1
  else:
    count[i] += 1

for ch in s:
  if ch in count:
    total.append(ch * count[ch])
    del count[ch]
    
    
if count:
  for i,j in count.items():
    total.append(i*j)

print(''.join(total))