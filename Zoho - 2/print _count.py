import re

def expand_string(s):
    pattern = r'\(([^()]*)\)\{(-?\d+)\}'  # Match (letters){number}
    
    while re.search(pattern, s):
        s = re.sub(pattern, lambda m: (m.group(1) * int(m.group(2))) if int(m.group(2)) > 0 else '', s)
    
    return s

# Test Cases
inputs = ["(z){-2}oho", "((X){2}(y){3}(z)){2}"]
for test in inputs:
    print(expand_string(test))
