def findsmallestMissingnum(num , left = None, right = None):
    if left is None and right is None:
      (left, right) = (0, len(num) - 1)

    if left > right:
       return left

    mid = left + (right - left) // 2
    if num[mid] == mid:
       return findsmallestMissingnum(num, mid + 1, right)

    else:
       return findsmallestMissingnum(num, left, mid - 1)

if __name__ == "__main__":
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"The smallest missing number is {findsmallestMissingnum(num)}")