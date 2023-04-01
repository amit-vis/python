# power of A
# def power_A(x,n):
#     if n==0:
#         return 1   #n=n*(n-1)*(n-2)
#     ans = x*power_A(x, n-1)
#     return ans

# ans = power_A(2, 4)
# print(ans)

#sum of array
# def sum_of_array(li):
#     if len(li)==1:
#         return li[0]
#     ans = li[0]+sum_of_array(li[1:])
#     return ans

# n = int(input())
# li = [int(i) for i in input().split()]

# print(sum_of_array(li))
def checkArray(li,ele):
    arr = len(li)
    if arr ==0:
        return False
    if li[0] ==ele:
        return True

    return checkArray(li[1:], ele)
    

n = int(input())
li = [int(i) for i in input().split()]
ele = int(input())
print(checkArray(li, ele))

