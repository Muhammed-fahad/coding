from itertools import combinations
def find_subsets(arr, target):
    for i in range(1, len(arr) + 1):  # Generate subsets of all sizes
        for subset in combinations(arr, i):  # itertools.combinations generates subsets
            if sum(subset) == target:  # Check sum condition
                print(list(subset))

# Input
arr = [2, 3, 5, 8, 10]
target = 10
print("Subsets with sum =", target, ":")
find_subsets(arr, target)


# def find_subsets(arr, target, index=0, current_subset=[]):
#     if sum(current_subset) == target:  # Valid subset found
#         print(current_subset)
#         return

#     if index >= len(arr) or sum(current_subset) > target:  # Base case
#         return

#     # Include the current element
#     find_subsets(arr, target, index + 1, current_subset + [arr[index]])

#     # Exclude the current element
#     find_subsets(arr, target, index + 1, current_subset)

# # Input
# arr = [2, 3, 5, 8, 10]
# target = 10
# print("Subsets with sum =", target, ":")
# find_subsets(arr, target)
