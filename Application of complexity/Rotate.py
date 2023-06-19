# def rotateArray(arr,d):
#     reverse(arr,0, d-1)
#     reverse(arr, d, len(arr)-1)
#     reverse(arr, 0, len(arr)-1)

# def reverse(arr,start,end):
#     while start<end:
#         arr[start],arr[end] = arr[end],arr[start]
#         start += 1
#         end -= 1
    
# t = int(input())  # Number of test cases

# for _ in range(t):
#     n = int(input())  # Size of the array/list
#     arr = list(map(int, input().split()))  # Elements of the array/list
#     d = int(input())  # Number of elements to rotate by

#     rotateArray(arr, d)
#     print(*arr)  # Print the rotated array/list


# another approach
# def rotateArray(arr,d):
#     l = []
#     for i in range(0,len(arr)):
#         l.append(arr[i])
#     arr.clear()
#     for i in range(d,len(arr)):
#         arr.append(l[i])
#     for j in range(0,d):
#         arr.append(l[j])

#     for i in range(len(arr)):
#         print(arr[i], end=' ')
#     return arr

def rotateArray(arr, d):
    n = len(arr)
    l = []
    for i in range(n):
        l.append(arr[i])

    arr.clear()
    for i in range(d, d+n):
        arr.append(l[i % n])  # Modulo operation to wrap around the index

    return arr

arr = [int(x) for x in input().split()]
d= int(input())
rotate_arr = rotateArray(arr,d)

for i in range(len(arr)):
    print(rotate_arr[i], end=' ')
