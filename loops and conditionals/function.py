# n = str('\U0001F600')
# for i in range(1,n+1):
#     print(i)
# factoriAl code using function

# def fact(n):
#     n_fact = 1
#     for i in range(1,n+1):
#         n_fact = n_fact*i
#     return n_fact

# n = int(input('Enter the n: '))
# r = int(input('Enter the r: '))
# n_fact = fact(n)
# r_fact = fact(r)
# n_r_fact = fact(n-r)
# ans = n_fact//(r_fact*n_r_fact)
# print(ans)

# check the prime number

# def isPrime(n):
#     for d in range(2, n+1):
#         if(n%d==0):
#             break
#     else:
#         return True
#     return False

# print(isPrime(20))

# def printPrime2ToN(n):
#     for k in range(2,n+1):
#         is_prime_k = isPrime(k)
#         if(is_prime_k):
#             print(k)
# (printPrime2ToN(20))

# scope variable
a1 = 10   #Global variable
def f1():
    b1 = 12 # Local variable
#     print(b1)

# print(a1)
# # Can't print a local variable out side the function
# f1()
# print(b1)

# a2 = 10   #Global variable
# def f2():
#     b2 = 12 # Local variable
#     print(b2)
#     print(a2) # we can call the global variable inside the local variable

# print(a2)
# f2()
# print(b2)
# def printTable(s,e,w):

#     while True:
#         c =0
#         if s<=e:
#             c = (s-32)*5//9
#             print(s,int(c))
#             s=s+w
#         else:
#             break

# s = int(input('Enter the s: '))
# e = int(input('Enter the e: '))
# step = int(input('Enter the w: '))

# printTable(s, e, step)

# def fibbo(n):
#     if (n==0 or n==1 or n==2):
#         return True
#     a =0
#     b =1
#     while b<n:
#         c= a+b
#         a = b
#         b =c
#     if b==n:
#         return True
#     return False

# n = int(input())
# if fibbo(n):
#     print('true')
# else:
#     print('false')

# check fibbonacci series

# def fibbonacci(n):
#     if (n==0 or n==1 or n==2):
#         return True
#     a=0
#     b=1
#     while b<n:
#         c=a+b
#         a=b
#         b=c
#         c=b
#     if (b==n):
#         return True
#     else:
#         return False
    
# n = int(input('Enter the number here: '))
# if fibbonacci(n):
#     print(True)
# else:
#     print(False)

# def palindrome(n):
#     temp = n
#     rev = 0
#     while 0<n:
#         dig=n%10
#         rev = rev*10+dig
#         n = n//10
#     if(temp==rev):
#         return True
#     return False

# if palindrome(n):
#     print(True)
# else:
#     print(False)

# ArmStrong number

def checkArm(n):
    sum = 0
    order = len(str(n))
    number = n
    while n>0:
        dig = n%10
        sum += dig**order
        n = n//10
    if number==sum:
        return True
    return False

n = int(input('Enter the number here: '))
if checkArm(n):
    print(True)
else:
    print(False)