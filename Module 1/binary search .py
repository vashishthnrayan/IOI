scores = [ 12, 25,33,41,50,67,72,85,91,95,98]
target = 95
lo ,hi,steps = 0, len(scores)-1, 0

while lo <= hi:
    mid= (lo + hi) // 2
    steps += 1
    if scores[mid] == target:
        print("Found at index ", mid,' | steps = ',steps)

        break

    elif scores[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1