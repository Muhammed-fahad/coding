def multi(val1, val2):
    result = 0
    place = 1
    
    while val2 > 0:
        digit2 = val2 % 10
        val2 //= 10
        
        carry = 0
        temp = 0
        inner_place = 1
        temp_val1 = val1
        
        while temp_val1 > 0:
            digit1 = temp_val1 % 10
            temp_val1 //= 10
            
            product = digit1 * digit2 + carry
            carry = product // 10
            product = product % 10
            
            temp += product * inner_place
            inner_place *= 10
        
        if carry > 0:
            temp += carry * inner_place
        
        result += temp * place
        place *= 10
    
    return result

val1 = int(input("Enter the number 1: "))
val2 = int(input("Enter the number 2: "))
print("Result:", multi(val1, val2))
