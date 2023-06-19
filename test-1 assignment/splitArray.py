def splitArray(arr, i, curr_sum):
    n = len(arr)
    total_sum = sum(arr)

    if i == n:
        return curr_sum == total_sum - curr_sum
    
    if splitArray(arr, i+1, curr_sum+arr[i]):
        return True
    if splitArray(arr, i+1, curr_sum):
        return True
    
    return False

arr = [int(x) for x in input().split()]

ans = splitArray(arr, 0, 0)

print(ans)