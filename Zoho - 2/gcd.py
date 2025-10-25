# Euclidean algorithm
def main():
    a = int(input("Enter number one: "))
    b = int(input("Enter number two: "))
    while b != 0:
        a, b = b, a % b
        
    print("GCD is:", a)
    return

main()