# 5432*
# 543*1
# 54*21
# 5*321
# *4321

# n = int(input('Enter the number here: '))
# for i in range(n):
#     for j in range(n):
#         if(j==n-i-1):
#             print('*',end='')
#         else:
#             print(n-j,end='')
#     print()

# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

n = int(input('Enter the number here: '))
for i in range(n):
    for j in range(2*n+1):
        if j==i+1-1 or j==n or j==2*n-i:
            print('*', end='')
        else:
            print(0, end='')
    print()

