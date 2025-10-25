a = [1, 2, 3, 4, 5, 3 ,3,3]
b = [2, 6, 3]

mini, maxi = (a,b) if len(a) < len(b) else (b,a)
count = 0
mini = list(set(mini))

for elem in mini:
    if elem in maxi:
        count += 1
print(count)

