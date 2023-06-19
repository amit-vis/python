# While loops
#Sum of n numbers

# n = int(input('Enter the Number here: '))
# sum = 0
# count = 1
# while count<=n:
#     sum = sum+count
#     count+=1

# print(sum)

# sum of the even number

# n = int(input('Enter the number here: '))
# sum = 0
# count = 2
# while count<=n:
#     sum = sum+count
#     count += 2
# print(sum)

# n = int(input('Enter a number: '))
# d = 2
# flag = True

# while d<n:
#     if(n%d==0):
#         flag = False
#     d = d+1

# if flag:
#     print('its prime')
# else:
#     print('not prime')

# d = 3
# if n % d == 0:
#     print('Red')

# else:
#     print('Yellow')

# print prime number

# k =2
# while k<=n:
#     d =2
#     flag = False
#     while d<k:
#         if k%d==0:
#             flag = True
#         d += 1
#     if not flag:
#         print(k)
#     k+=1

# celsius to fareinheite conversion code

# s = int(input('Enter the s: '))
# e = int(input('Enter the e: '))
# step = int(input('Enter the step: '))

# c=s
# while c<=e:
#     f=((c-32)*5)/9
#     print(f'{f}',{c})
#     c=c+step

# reverse a number

# n = int(input('enetr the number: '))
# num = n
# rev = 0
# while n>0:
#     sum= n%10
#     rev = rev*10+sum
#     n=n//10

# print(rev)

# palindrome number
# n = int(input('Enter the number:'))
# num = n
# rev = 0
# while n>0:
#     a = n%10
#     print('here is the value of a: ',a)
#     rev = rev*10+a
#     print('here is the value of rev: ',rev)
#     n = n//10
#     print('here is the value of n: ',n)

#     print(rev)

# if(num==rev):
#     print(True)
# else:
#     print(False)

# Nth fibbonacci number

n=int(input())
a=0
b=1
c=0
count = 1
while count<=n:
    a=b
    print('value of a: ',a)
    b=c
    print('value of b: ',b)
    c=a+b
    print('value of c:',c)
    count+=1
print(c)
