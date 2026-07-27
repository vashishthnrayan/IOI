# My Train Seat Finder
# Analysis and Space Complexity

# Step 1: Create the Sorted Seat List
seat_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

# Step 2: Set the Target Seat
target = 130


# Step 3: Iterative Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


# Step 6: Recursive Binary Search
def recursive_binary_search(arr, low, high, target, steps=1):
    if low > high:
        return -1, steps - 1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid, steps

    elif arr[mid] > target:
        return recursive_binary_search(arr, low, mid - 1, target, steps + 1)

    else:
        return recursive_binary_search(arr, mid + 1, high, target, steps + 1)


# Run Iterative Search
index1, steps1 = binary_search(seat_numbers, target)

print("===== ITERATIVE BINARY SEARCH =====")
if index1 != -1:
    print("Seat Found!")
    print("Seat Number :", target)
    print("Index :", index1)
    print("Steps Taken :", steps1)
else:
    print("Seat Not Found")

print()

# Run Recursive Search
index2, steps2 = recursive_binary_search(
    seat_numbers, 0, len(seat_numbers) - 1, target)

print("===== RECURSIVE BINARY SEARCH =====")
if index2 != -1:
    print("Seat Found!")
    print("Seat Number :", target)
    print("Index :", index2)
    print("Steps Taken :", steps2)
else:
    print("Seat Not Found")

print()

# Step 5 & Step 7: Complexity Analysis
print("===== COMPLEXITY ANALYSIS =====")
print("Iterative Binary Search")
print("Time Complexity : O(log n)")
print("Space Complexity : O(1)")

