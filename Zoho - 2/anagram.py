# a = input("Enter a number: ")
# b = input("Enter a number: ")

# aStore={}
# bStore = {}

# if(len(a) == len(b)):
#   for i in range(len(a)):
#     if a[i] in aStore:
#       aStore[a[i]] += 1
#     else:
#       aStore[a[i]] = 0
    
#     if b[i] in bStore:
#       bStore[b[i]] += 1
#     else:
#       bStore[b[i]] = 0

# for i,j in aStore.items():
#   if i not in bStore:
#     print("Not anagram")
#     break
#   else:
#     if bStore[i] != j:
#       print("Not anagram")
#       break

# if(len(a) == len(b)):
#   print("anagram")


a = input("Enter a string: ")
b = input("Enter a string: ")

aStore = {}
bStore = {}

if len(a) != len(b):
    print("Not anagram")
else:
    for i in range(len(a)):
        aStore[a[i]] = aStore.get(a[i], 0) + 1
        bStore[b[i]] = bStore.get(b[i], 0) + 1

    if aStore == bStore:
        print("Anagram")
    else:
        print("Not anagram")


from collections import Counter
a = input("Enter first string: ").replace(" ", "").lower()
b = input("Enter second string: ").replace(" ", "").lower()
print("Anagram" if Counter(a) == Counter(b) else "Not anagram")
