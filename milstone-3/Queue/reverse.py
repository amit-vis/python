
# def reverseQueue(queue):
#     if len(queue) == 0:
#         return
#     front = queue.pop(0)
#     reverseQueue(queue)
#     queue.append(front)


# def process_test_case():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         ele = list(map(int, input().split()))

#         reverseQueue(ele)

#         for element in ele:
#             print(element, end=' ')
#         print()

# process_test_case()

# reverse k elements
def reverseK(queue, k):
    stack = []

    for _ in range(k):
        stack.append(queue.pop())

    while stack:
        queue.insert(0, stack.pop())

n,k = map(int, input().split())

queue = list(map(int, input().split()))

reverseK(queue, k)

for ele in queue:
    print(ele, end=' ')
print()
