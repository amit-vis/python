# arr = [1,2,5,6,3]
# for i in range(len(arr)):
#     print(arr[i])

def sumOfTwo(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
    return None


arr = [int(x) for x in input().split()]
target = int(input())

print(sumOfTwo(arr, target))