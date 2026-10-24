
# Rotate My Scores - Array Problems 1

# Original list of scores
scores = [10, 20, 30, 40, 50]

# 1. Reverse a list using two pointers
def reverse_list(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# 2. Reverse elements in fixed-size groups
def reverse_groups(arr, k):
    for i in range(0, len(arr), k):
        arr[i:i+k] = arr[i:i+k][::-1]
    return arr


# 3. Left rotate a list by one position
def left_rotate_one(arr):
    if len(arr) > 0:
        first = arr.pop(0)
        arr.append(first)
    return arr


# 4. Left rotate a list by n positions
def left_rotate_n(arr, n):
    if len(arr) > 0:
        n = n % len(arr)
        arr[:] = arr[n:] + arr[:n]
    return arr


# 5. Find leaders in an array
def find_leaders(arr):
    leaders = []
    max_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    leaders.reverse()
    return leaders


# Display results
print("Original scores:", scores)

print("1. Reversed:", reverse_list(scores.copy()))

print("2. Group reversal (k=2):",
      reverse_groups(scores.copy(), 2))

print("3. Left rotation by 1:",
      left_rotate_one(scores.copy()))

print("4. Left rotation by 2:",
      left_rotate_n(scores.copy(), 2))

print("5. Leaders:",
      find_leaders([16, 17, 4, 3, 5, 2]))
