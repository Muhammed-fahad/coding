def prime_check(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

n = int(input("Enter a Number: "))
print("Prime" if prime_check(n) else "Not Prime")
