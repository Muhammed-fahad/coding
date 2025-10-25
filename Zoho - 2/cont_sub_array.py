def max_subarray_sum(arr):
    maxsal = float('-inf')
    currentSum = 0
    for i in arr:
        currentSum+=i
        maxsal = max(currentSum,maxsal)
        if(currentSum < 0):
            currentSum = 0
    return maxsal

arr = list(map(int, input("Enter the array elements: ").split()))
arr1 = [-2, 1, -3, 4, -1, 2, 1,-5,-4, 4]
print("Maximum subarray sum: ", max_subarray_sum(arr1))