# def reverse(li):
#     length = len(li)
#     for i in range(length//2):
#         li[i],li[length-i-1]=li[length-i-1],li[i]

# n = int(input('Enter the row number: '))
# li = [int(x) for x in input().split()]
# reverse(li)
# print(li)

# li = [2,4,5,3,4]

# print(li[3::-1])
# print(li[3:1:-1])
# print(li[::-1])
# print(li[:1:-1])
# print(li[1:-5:-1])

# def findUnique(arr):
#     count = 100
#     for i in arr:
#         if arr.count(arr[i])<count:
#             count = arr.count(arr[i])
#             res = arr[i]
#     return res

# def findDuplicate(arr):
#     count = 1
#     for i in arr:
#         if arr.count(arr[i])>count:
#             count = arr.count(arr[i])
#             res = arr[i]
#     return res

# n = int(input())
# arr = [int(x) for x in input().split()]
# print(findDuplicate(arr))

import sys

# intersection of the two array
# def intersectionTwoArray(arr,arr2):
#     for i in range(len(arr)):
#         for j in range(len(arr2)):
#             if arr[i]==arr2[j]:
#                 print(arr[i],end=' ')
#                 arr2[j]=sys.maxsize
#                 break
# n1 = int(input('Enter the arr count: '))
# arr = [int(x) for x in input().split()]
# n2 = int(input("Enter the arr2 count: "))
# arr2 = [int(k) for k in input().split()]
# print(intersectionTwoArray(arr, arr2))

# def intersection_Two_Array(arr1,arr2):
#     set1 = set(arr1)
#     set2 = set(arr2)
#     intersection_point = set1.intersection(set2)
#     return list(intersection_point)

# n1 = int(input('Enter the arr count: '))
# arr1 = [int(x) for x in input().split()]
# n2 = int(input("Enter the arr2 count: "))
# arr2 = [int(k) for k in input().split()]
# print(intersection_Two_Array(arr1, arr2))

# pair sum approach

# def pair_sum(arr,x):
#     num =0
#     for i in arr:
#         for j in range(i+1,len(arr)-1):
#             if arr[i]+arr[j]==x:
#                 num +=1
#     return num

# tripple sum approach
# def triplet_sum(arr,x):
#     num = 0
#     for i in arr:
#         for j in range(i+1,len(arr)-1):
#             for k in range(j+1,len(arr)-2):
#                 if arr[i]+arr[j]+arr[k]==x:
#                     num +=1
#     return num

# n1 = int(input('Enter the arr count: '))
# arr = [int(x) for x in input().split()]
# x = int(input("Enter the number: "))
# print(triplet_sum(arr, x))

def Sort_Binary(arr):
    s = 0
    e = len(arr)-1
    while s<e:
        if arr[s]==0 and arr[e]==1:
            arr[s],arr[e]=arr[e],arr[s]
            s +=1
            e -=1
        elif arr[s]==1 and arr[e]==0:
            s+=1
            e-=1
        elif arr[s]==1:
            s+=1
        else:
            e-=1
    return arr[::-1]

n = int(input('Enter the number: '))
arr = [int(x) for x in input().split()]
print(Sort_Binary(arr))
        