# li = [1,'Amit',6.8,9,8]
# # for i in li:
# #     print(i)

# for i in range(len(li)):
#     print(li[0:i])

# n = int(input())

# li = []

# for i in range(n):
#     curr = int(input())
#     li.append(curr)

# print(li)

# for ele in li:
#     print(ele)

# li = [int(i) for i in input().split()]
# print(li)

N = int(input())
li = [int(i) for i in input().split()]
sum = 0
for ele in li:
    sum = sum +ele
print(sum)