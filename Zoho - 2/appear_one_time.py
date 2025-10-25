nums = list(map(int, input("Enter numbers: ").split(' ')))
result = 0
for i in nums:
    result ^= i
print(result)
