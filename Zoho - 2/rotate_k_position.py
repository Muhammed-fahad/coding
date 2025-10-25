value = str(input())
n = int(input())

value_stored = value[-n:] + value[:len(value)-(n)]
print(value_stored)
