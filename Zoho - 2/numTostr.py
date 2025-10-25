# 1123
# {1, 1, 2, 3} = aabc
# {11, 2, 3} = kbc
# {1, 1, 23} = aaw
# {11, 23} = kw

def number_to_codes(number):
  a = []    
  for i in number:
    a.append(chr(ord(i) - ord('0') + 96))
  
  for i in range((len(number)//2)+1):
    b = number[i:i+2]
    b = int(b)
    chr(96+b)
    
# Example usage:
number = "1123"
codes = number_to_codes(number)
print("".join(codes))