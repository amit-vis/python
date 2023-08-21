def pairSumDiff(arr, k):
    if k <0:
        return 0
    d = {}
    for i in arr:
        d[i] = d.get(i,0) +1

    count = 0
    if k ==0:
        for value in d.values():
            if value>1:
                count += value * (value -1)//2
        return count
    
    for num in d:
        if num+k in d:
            count += d[num] * d[num+k]
    return count

arr = [int(x) for x in input().split()]
k = int(input())
print(pairSumDiff(arr, k))