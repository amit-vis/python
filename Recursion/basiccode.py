# power of n
# def power(n,m):
#     if m ==0:
#         return 1
#     return n*power(n,m-1)

# n = int(input('Enter the base here: '))
# m = int(input('Enter the power here: '))
# print(power(n,m))

# factorial number

# def fact(n):
#     if n ==0:
#         return 1
#     return n* fact(n-1)

# fibbonacci series

# def fibbonacci(n):
#     if n == 0:
#         return 0
#     if n ==1:
#         return 1
#     return fibbonacci(n-1)+fibbonacci(n-2)

# n = int(input('Enter the base here: '))
# print(fibbonacci(n))

# number series
# def number(n):
#     if n == 0:
#         return
#     print(n)
#     number(n-1)
#     print(n)
#     return

# number(10)

# sum of the series

# def sum_number(n):
#     if n ==0:
#         return 0
#     if n == 1:
#         return 1
#     return n+sum_number(n-1)

# n = int(input('enter the number: '))
# print(sum_number(n))

# list is sorted or not
# def isSorted(a):
#     if len(a)<=1:
#         return True
#     if a[0]>a[1]:
#         return False
#     return isSorted(a[1:])

# a = [int(x) for x in input().split()]
# print(isSorted(a))

def sumArray(a):
    if len(a)==1:
        return a[0]
    return a[0]+sumArray(a[1:])

a = [int(x) for x in input().split()]
print(sumArray(a))