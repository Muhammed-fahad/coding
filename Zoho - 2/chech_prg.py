def odd_even(num):
    if(int(num)%2 == 0):
        return True
    else:
        return False
    
nums = list(map(odd_even , input("Enter the num: ").split(' ')))
print(nums)