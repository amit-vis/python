# 1 2 3 4 5 
# 11 12 13 14 15
# 21 22 23 24 25
# 16 17 18 19 20
# 6 7 8 9 10

# print the patterns
# n = int(input('Enter the number here'))
# int_func = [[0 for i in range(n)] for j in range(n)]
# a = 0
# b = n-1
# c = 1
# for i in range(n):
#     if i%2==0:
#         for j in range(n):
#             int_func[a][j]=c
#             c+=1
#         a+=1
#     else:
#         for j in range(n):
#             int_func[b][j] = c
#             c+=1
#         b-=1




# for i in range(n):
#     for j in range(n):
#         print(int_func[i][j], end=' ')
#     print()

# rectangular patterns
# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4 

# n = int(input('Enter the number here'))

# k = 2*n-1
# low = 0
# high = k-1
# value = n
# int_func = [[0 for i in range(k)] for j in range(k)]

# for i in range(n):
#     for j in range(low, high+1):
#         int_func[i][j] = value

#     for j in range(low+1,high+1):
#         int_func[j][i]= value

#     for j in range(low+1,high+1):
#         int_func[high][j]= value

#     for j in range(low+1, high):
#         int_func[j][high] = value

#     low +=1
#     high -=1
#     value -=1

# for i in range(k):
#     for j in range(k):
#         print(int_func[i][j], end=' ')
#     print()

#   *
#  ***
# *****
#  ***
#   *
n = int(input('enter the number: '))
n1 = (n+1)//2
for i in range(1,n1+1):
    for space in range(n1-i):
        print(' ',end='')
    for j in range(i,2*i):
        print('*',end='')
    for j in range(i,2*i-1):
        print('*', end='')
    print()

n2 = n1-1
for i in range(n2):
    for space in range(i+1):
        print(' ', end='')
    for j in range(2*(n2-i)-1):
        print('*', end='')
    print()