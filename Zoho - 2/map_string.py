# str1 = egg
# str2 = abb  || correct

def main():
    store = {}
    reverse_store = {}
    
    a = input("Enter string 1: ")
    b = input("Enter string 2: ")
    
    if len(a) != len(b):
        print("Not isomorphic")
        return 0

    for i in range(len(a)):
        ch1 = a[i]
        ch2 = b[i]

        if ch1 in store:
            if store[ch1] != ch2:
                print("Not isomorphic")
                return 0
        else:
            if ch2 in reverse_store:
                print("Not isomorphic")
                return 0
            store[ch1] = ch2
            reverse_store[ch2] = ch1

    print("Isomorphic")
    return
main()