a = "cat"
b = "tacae"

a1 = {}
a2 = {}
if(len(a) == len(b)):
  for i in range(len(a)):
    if a[i] in a1:
      a1[a[i]] += 1
    else:
      a1[a[i]] = 1

    if b[i] in a2:
      a2[b[i]] += 1
    else:
      a2[b[i]] = 1
