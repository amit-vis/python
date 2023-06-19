# power solution reducing the time complexity and space complexity
# first way to reduce of recursion solution
# def power(x,n):
#     if n ==0:
#         return 1
#     if n== 1:
#         return x
#     return x*power(x,n-1)

# def power(x,n):
#     if n ==0:
#         return 1
#     small_cal = power(x,n//2)
#     if n%2==0:
#         return small_cal * small_cal
#     else:
#         return x*small_cal*small_cal

# iterative solution

    

# x = int(input('Enter the number: '))
# n = int(input('Enter the number: '))
# print(power(x,n))


# n = int(input('Enter the number: '))
# x = int(input('Enter the number: '))
# i = 0
# ans = 1

# while i < n:
#     ans = ans * x
#     i += 1

# print(ans)

# code for array intersation
# iterative solution
# def IntersectionArray(arr1,arr2,n,m):
#     arr1.sort()
#     arr2.sort()
#     i,j=0,0
#     arr = []
#     while i<n and j < m:
#         if arr1[i]<arr2[j]:
#             i+=1
#         elif arr1[i]>arr2[j]:
#             j+=1
#         else:
#             arr.append(arr1[i])
#             i+=1
#             j+=1
#     for i in arr:
#         print(i, end='')

# Recursive solution
# def recursiveIntersection(arr1,arr2,m,n):
#     arr1.sort()
#     arr2.sort()

#     return Intersection(arr1,arr2,m,n,0,0,[])

# def Intersection(arr1,arr2,m,n,i,j,arr):
#     if i>=m or j>=n:
#         return arr
    
#     if arr1[i]<arr2[j]:
#         return Intersection(arr1,arr2,m,n,i+1,j,arr)
#     if arr1[i]>arr2[j]:
#         return Intersection(arr1,arr2,m,n,i,j+1,arr)
#     else:
#         arr.append(arr1[i])
#         return Intersection(arr1,arr2,m,n,i+1,j+1,arr)

# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# print(recursiveIntersection(arr1, arr2, len(arr1), len(arr2)))

# Equilibrium Index Itrative approach
# def Equilibrium(arr):
#     total_sum = sum(arr)

#     left_sum = 0
#     for i in range(len(arr)):
#         total_sum -= arr[i]
#         if left_sum == total_sum:
#             return i
#         left_sum += arr[i]
#     return -1

# Equilibrium solution using recursion
# def Equilibrium(arr):
#     total_sum = sum(arr)
#     return EquilibriumRec(arr,0,0,total_sum)
# def EquilibriumRec(arr, index, left_sum,total_sum):
#     if index == len(arr):
#         return left_sum == total_sum
#     total_sum -= arr[index]
#     if left_sum == total_sum:
#         return index
#     else:
#         return EquilibriumRec(arr, index+1, left_sum+arr[index], total_sum)

# another approach of the equilibrium
# 
# find a unique
# def find_unique_number(arr,n):
#     if n ==0:
#         return None
#     unique_number = find_unique_number(arr, n-1)
#     if arr[n-1] not in arr[:n-1]:
#         return arr[n-1]
#     else:
#         return unique_number


# # Test the function
# array = [6, 1, 6, 3, 4, 3, 1]
# unique_number = find_unique_number(array,len(array))
# print(f"The unique number in the array is: {unique_number}")

# def unique_number(arr):
#     if len(arr)==0:
#         return None
#     unique_number = unique_number(len(arr)-1)
#     if arr[len(arr)-1] not in arr[:len(arr)-1]:
#         return len(arr)-1
#     else:
#         return unique_number

# array = [6, 1, 6, 3, 4, 3, 1]
# unique_number = unique_number(array)
# print(f"The unique number in the array is: {unique_number}")

# def unique_number(arr):
#     ansXor = 0
#     for i in arr:
#         ansXor = ansXor^i
#     return ansXor

# array = [int(x) for x in input().split()]
# result = unique_number(array)
# print(f"The unique number in the array is: {result}")

# def sum_arr(arr):
#     sum_of_arr = sum(arr)
#     natural_num = ((len(arr)-2)*(len(arr)-1)//2)
#     return sum_of_arr - natural_num

# def sum_arr(arr):
#     arr.sort()
#     i = 0
#     j = len(arr)-1
#     while i<j:
#         if arr[i]+arr[j]==0:
#             return arr[i],arr[j]
#         elif arr[i]+arr[j]<0:
#             i +=1
#         else:
#             j -= 1
#     return -1

# triplet sum code
def triplet_sum(arr, X):
    arr.sort()
    count = 0
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == X:
                count += 1
                left += 1
                right -= 1
            elif current_sum < X:
                left += 1
            else:
                right -= 1
    return count

t = int(input())

for _ in range(t):
    # Read the size of the array/list
    n = int(input())

    # Read the elements of the array/list
    arr = list(map(int, input().split()))

    # Read the target sum
    X = int(input())

    # Find and print the number of triplets
    triplets_count = triplet_sum(arr, X)
    print(triplets_count)
