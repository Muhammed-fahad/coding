def check_count(arr):
    store = {}
    for i in arr:
        store[i] = store.get(i , 0) + 1
    return store

arr = list(input("Enter the number: ").split(" "))
print(check_count(arr))