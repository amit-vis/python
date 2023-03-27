# square of star patterns nth * using while loop
# *****
# *****
# *****
# *****

# n = int(input())
# i = 0
# while n>=i:
#     j=0
#     while j<=n:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

# square of star patterns nth * using while loop

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*',end='')
#         j+=1
#     print()
#     i+=1
# ======================================================================================================================================================
# patterns
# 1234
# 1234
# 1234
# 1234

# using while loop
# n = int(input('Enter the number: '))
# i = 0
# while n>i:
#     j = 0
#     while j<n:
#         print(j+1, end='')
#         j+=1
#     print()
#     i+=1

# using for loop

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         print(j+1,end='')
#         j+=1
#     print()
#     i+=1

# 1111
# 2222
# 3333
# 4444

# n = int(input('Enter the number here: '))
# i =0
# while n>i:
#     j=0
#     while j<n:
#         print(i, end='')
#         j+=1
#     print()
#     i+=1

# n = int(input('Enter the number here: '))
# for i in range(n):
#     for j in range(n):
#         print(i+1, end='')
#         j+=1
#     print()
#     i+=1

# 4321
# 4321
# 4321
# 4321

# n = int(input('Enter the number here:'))
# i=1
# while n>i:
#     j=1
#     while j<=n:
#         print(n-j+1,end='')
#         j+=1
#     print()
#     i+=1

# n = int(input('Enter the number here:'))
# for i in range(n):
#     for j in range(n):
#         print(n-j, end='')
#         j+=1
#     print()
#     i+=1

# 4444
# 3333
# 2222
# 1111

# n = int(input('Enter the number here:'))
# i = 1
# while i<=n:
#     j=1
#     while j<=n:
#         print(n-i+1,end='')
#         j+=1
#     print()
#     i+=1
# n = int(input('Enter the number here:'))
# for i in range(n):
#     for j in range(n):
#         print(n-i, end='')
#         j+=1
#     print()
#     i+=1

# triangle patterns
# *
# **
# ***
# ****

# n = int(input('Enter the number here:'))
# i = 1
# while i<=n:
#     j=1
#     while j<=i:
#         print('*', end='')
#         j+=1
#     print()
#     i+=1

# using for loop

# n = int(input('Enter the number here:'))
# for i in range(n+1):
#     for j in range(i):
#         print('*', end='')
#         j+=1
#     print()
#     i+=1

# for i in range(6):
#     for j in range(7):
#         if(i==0 and j%3 != 0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print()

# 1
# 21
# 321
# 4321

# n = int(input('Enter the number here:'))
# i=1
# while n>=i:
#     j=1
#     while j<=i:
#         print(i-j+1,end='')
#         j+=1
#     i+=1
#     print()

# 1
# 11
# 202
# 3003
# n = int(input('Enter the number here:'))

# i =1
# print(1)
# while i<=n-1:
#     j=1
#     while j<=i+1:
#         if (j==1 or j == i+1):
#             print(i, end='')
#         else:
#             print(0, end='')
#         j+=1
#     print()
#     i+=1

# using for loop

# n = int(input('Enter the number here:'))

# print(1)

# for i in range( n+1):
#     for j in range(i+1):
#         if j == 1 or j == i:
#             print(i, end="")
#         else:
#             print("0", end="")
#     print()

# ****
# ***
# **
# *

# n = int(input("Enter the number here:"))
# i =1
# while i<=n:
#     j=1
#     while j<=n-i+1:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     print()
#     i+=1

# i=1
# while i<=n:
#     spaces =1
#     while spaces<=n-i:
#         print(' ',end='')
#         spaces+=1
#     j=1
#     while j<=i:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

# for i in range(n):
#     for spaces in range(n-i):
#         print(' ', end='')
#     for j in range(i+1):
#         print('*', end='')
#     print()

# i =1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end='')
#         j=j+1
#     spaces = 1
#     while spaces<=2*n-2*i:
#         print(' ',end='')
#         spaces+=1
#     j=1
#     while j<i+1:
#         print(i-j+1,end='')
#         j+=1
#     print()
#     i+=1

# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end='')
#     for spaces in range(2*n-2*i-1):
#         print(' ', end='')
#     for j in range(i+1):
#         print(i-j+1,end='')
#     print()

# 33333
# 32223
# 32123
# 32223
# 33333

# n= int(input('Enter the number: '))
# k =2*n-1
# low = 0
# high = k-1
# value = n

# matrix = [[0 for i in range(k)]for j in range(k)]
# for i in range(n):
#     for j in range(low,high+1):
#         matrix[i][j] = value
#     for j in range(low+1,high+1):
#         matrix[j][i]= value
#     for j in range(low+1, high+1):
#         matrix[high][j]= value
#     for j in range(low+1, high):
#         matrix[j][high] = value
    


#     low = low+1
#     high = high-1
#     value = value-1

# for i in range(k):
#     for j in range(k):
#         print(matrix[i][j], end='')
#     print()

#  ***
# *    *
# ******
# *    *
# *    *

# for i in range(7):
#     for j in range(5):
#         if ((j==0 or j==4) and i !=0 ) or (i==0 or i==3) and (j>0 and j<4):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

for i in range(7):
    for j in range(5):
        if (j==0) or (j==4 and i!=0 and i!=3 and i!=6) or ((i ==0 or i==3 or i == 6) and (j>0 and j<4)):
            print('*', end='')
        else:
            print(' ', end='')
    print()
    




