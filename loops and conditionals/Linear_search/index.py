# n = int(input())
# li = [int(x) for x in input().split()]
# flag = False
# ele = int(input())

# for i in range(len(li)):
#     if(li[i]==ele):
#         print(i)
#         flag = True
#         break
# if flag is False:
#     print(-1)
# else:
#     print(1)

# linear serch using function

def linearSearch(li,ele):
    for i in range(len(li)):
        if li[i]==ele:
            return i
    return -1

n = int(input())
li = [int(x) for x in input().split()]

index = linearSearch(li, 5)
print(index)