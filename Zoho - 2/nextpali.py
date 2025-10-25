# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# def next_palindrome(n):
#     n += 1
#     while not is_palindrome(n):
#         n += 1
#     return n

# num = int(input("Enter a number: "))
# print("Next smallest palindrome:", next_palindrome(num))



def next_palindrome(n):
    # 12345
    
    num_str = str(n)
    length = len(num_str)
    
    left_half = num_str[:(length + 1) // 2]
    mirrored = left_half + left_half[:-1][::-1]
    
    if(int(mirrored) > n):
        return int(mirrored)
    
    left_half = str(int(left_half) + 1)
    mirrored = left_half + left_half[:-1][::-1]
    
    return int(mirrored)
        

num = int(input("Enter a number: "))
print("Next smallest palindrome:", next_palindrome(num))