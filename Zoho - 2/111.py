def convertToWave(arr):
    n = len(arr)    
    for i in range(0, n - 1, 2):
        if i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Example Input
arr = [10, 90, 49, 2, 1, 5, 23] # [90, 10, 49, 1, 5, 2, 23]
convertToWave(arr)
print("Wave Array:", arr) 