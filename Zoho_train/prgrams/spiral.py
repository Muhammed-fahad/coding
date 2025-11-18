def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])

    while top < bottom and left < right:
        # Traverse from left to right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        # Traverse from right to left
        if top < bottom:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

        # Traverse from bottom to top
        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Test
matrix = [
  [1,  2,  3,  4],
  [5,  6,  7,  8],
  [9, 10, 11, 12]
]

print(*spiral_order(matrix))
