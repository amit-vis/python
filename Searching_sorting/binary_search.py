def binary_sort(arr,n):
    l = 0
    u = len(arr)-1
    while l<=u:
        m = (l+u)//2
        if arr[m]==n:
            return m
        elif arr[m]<n:
            l+=1
        else:
            u -=1
    return -1

arr = [int(x) for x in input().split()]
n = int(input('Enter the number'))

print(binary_sort(arr, n))