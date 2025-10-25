array = [1,2,4,5,6]
n = len(array)+1
exp = (n*(n+1))//2
act = sum(array)
mis = exp - act
print(mis)