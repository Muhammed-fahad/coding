def is_fibonacci(n):
    if n == 0 or n == 1:
        return True

    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

numbers = list(map(int, input("Enter numbers: ").split()))
fib_numbers = [num for num in numbers if is_fibonacci(num)]
print("Fibonacci numbers:", fib_numbers)
