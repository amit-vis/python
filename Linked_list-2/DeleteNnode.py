# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def deleteNnode(head,M,N):
#     if head is None:
#         return head
#     if M ==0 :
#         return None
#     if N == 0:
#         return head
#     t1 = head
#     count1 = 1
#     count2 = 1
#     while t1 is not None:
#         while count1<m:
#             count1 +=1
#             t1 = t1.next
#         if t1 is None:
#             return head
#         t2 = t1.next
#         while count2<=n:
#             count2 +=1
#             if t2 is None:
#                 break
#             t2 = t2.next
#         t1.next = t2
#         t1 = t2
#         count2 = 1
#         count1 = 1
#     return head
     

# def printLL(head):
#     while head is not None:
#         print(str(head.data) + '->', end='')
#         head = head.next
#     print(None)
#     return

# def takeInput():
#     linkList = [int(x) for x in input().split()]
#     head = None
#     tail = None
#     for currData in linkList:
#         if currData == -1:
#             break
#         newNode = Node(currData)
#         if head is None:
#             head = newNode
#             tail = newNode
#         else:
#             tail.next = newNode
#             tail = newNode
#     return head

# head = takeInput()
# printLL(head)
# m = int(input("Enter the m: "))
# n = int(input("Enter the n: "))
# head = deleteNnode(head, m, n)
# printLL(head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteNnode(head, m, n):
    if head is None:
        return head
    if m ==0:
        return None
    if n == 0:
        return head
    t1 = head
    count1 = 1
    count2 = 2
    while t1 is not None:
        while count1 < m:
            count1 += 1
            t1 = t1.next
            if t1 is None:
                return head
        t2 = t1.next
        while count2<=n:
            count2 +=1
            if t2 is None:
                break
            t2 = t2.next
        t1.next = t2
        t1 = t2
        count1 = 1
        count2 = 1
    return head


def printLL(head):
    while head is not None:
        print(str(head.data) + '->', end='')
        head = head.next
    print(None)
    return
def takeInput():
    linkList = [int(x) for x in input().split()]
    head = None
    tail = None
    for currData in linkList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
head = takeInput()
printLL(head)
m = int(input("Enter the number: "))
n = int(input("Enter the n number: "))
head = deleteNnode(head, m, n)
printLL(head)