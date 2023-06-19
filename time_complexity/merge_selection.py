import time
# selction sort 
def selectionSort(a):
    for i in range(len(a)):
        mid_index = i
        for j in range(i+1, len(a)):
            if a[mid_index]>a[j]:
                mid_index = j
        a[i],a[mid_index]= a[mid_index],a[i]
    return a

# a = [int(i) for i in input().split()]
# print(selectionSort(a))

# merge sort
def merge(a1,a2,a):
    i = 0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k] = a1[i]
            i = i+1
            k = k+1
        else:
            a[k] = a2[j]
            j = j+1
            k=k+1
    while i<len(a1):
        a[k] = a1[i]
        i=i+1
        k=k+1
    while j<len(a2):
        a[k] = a2[j]
        j = j+1
        k = k+1

def mergeSort(a):
    if len(a)==0 or len(a)==1:
        return
    mid = len(a)//2
    a1 = a[0:mid]
    a2 = a[mid:]
    mergeSort(a1)
    mergeSort(a2)

    merge(a1, a2, a)
    return a


# a = [int(i) for i in input().split()]
# print(mergeSort(a))

def create_rev_array(n):
    a = []
    for i in range(n,0,-1):
        a.append(i)
    return a


# a = int(input('Enter the number: '))
# n = create_rev_array(a)
# start = time.time()
# mergeSort(n)
# end = time.time()
# print(a, end-start)

# n = create_rev_array(a)
# start = time.time()
# selectionSort(n)
# end = time.time()
# print(a, end-start)

# bubble sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

# a = [int(i) for i in input().split()]
# print(bubbleSort(a))

# binary search

def binary_search(a,k):
    low = 0
    high = len(a)-1
    while low<=high:
        mid = (low+high)//2
        if a[mid]==k:
            return mid
        elif a[mid]>k:
            mid = mid-1
        else:
            mid = mid+1
    return -1

# a = [int(i) for i in input().split()]
# k = int(input('Enter the number: '))
# print(binary_search(a, k))

# linear search

def linear_search(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1

a = [int(i) for i in input().split()]
k = int(input('Enter the number: '))
print(binary_search(a, k))