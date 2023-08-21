def largestSubzero(arr):
    ans = 0
    sum = 0
    d= {}
    d[0] = -1
    for i in range(len(arr)):
        sum += arr[i]
        if sum in d:
            ans = max(ans, i-d[sum])
        else:
            d[sum] = i
    return ans

arr = [int(x) for x in input().split()]

print(largestSubzero(arr))