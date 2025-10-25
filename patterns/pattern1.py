def print_pattern(n):
    for i in range(n):
        for j in range(n):
            value = n - min(i, j, n-1-i, n-1-j)
            print(value, end=' ')
        print()

n = 6
print_pattern(n)