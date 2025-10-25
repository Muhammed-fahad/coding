s = "greeksforgeeks"
counting = [0] * 26

for i in s:
  v = ord(i) - 97
  counting[v] += 1

s = ""

for i in range(len(counting)):
  if counting[i] != 0:
    val = chr(i+97) * counting[i]
    s +=val
print(s)
print("".join(sorted(s)))