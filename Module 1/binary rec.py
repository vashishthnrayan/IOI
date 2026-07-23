def binary_search_rec(scores,lo,hi,target,call = 0):
    call += 1
    if lo > hi:
     
        return -1,call

    mid = (lo + hi) // 2
    if scores[mid] == target:
        
        return mid,call

    elif scores[mid] < target:
        return binary_search_rec(scores,mid+1,hi,target,call)
    else:
        return binary_search_rec(scores,lo,mid-1,target,call)

scores = [ 12, 25,33,41,50,67,72,85,91,95,98]
result,call = binary_search_rec(scores , 0 , 10 , 98)
print("Found at index ", result,' | steps = ',call)