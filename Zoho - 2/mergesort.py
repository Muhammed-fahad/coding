def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]  # Left half of the array
    right_half = arr[mid:]  # Right half of the array
    
    # Step 2: Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Step 3: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []  # Resultant sorted array
    i = j = 0  # Pointers for left and right arrays
    
    # Merge the two arrays by comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)