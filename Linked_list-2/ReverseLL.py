# Reverse Linked List recursive solution
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# # def reverseLL(head):
# #     if head == None:
# #         return head
# #     if head.next == None:
# #         return head
# #     smallHead = reverseLL(head.next)
# #     head.next.next = head
# #     head.next = None
# #     return smallHead

# # another approach
# # def reverseLL(head):
# #     if head is None or head.next is None:
# #         return head
# #     smallHead = reverseLL(head.next)
# #     curr = smallHead
# #     while curr.next is not None:
# #         curr = curr.next

# #     curr.next = head
# #     head.next = None
# #     return smallHead

# # def reverseLL(head):
# #     if head.next is None:
# #         return head, head
# #     SH, ST = reverseLL(head.next)
# #     ST.next = head
# #     head.next = None
# #     return SH,head

# def reverseLL2(head):
#     if head is None or head.next is None:
#         return head
#     smallHead = reverseLL2(head.next)
#     tail = head.next
#     tail.next = head
#     head.next = None
#     return smallHead

# def printLL(head):
#     while head is not None:
#         print(str(head.data)+"->", end="")
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
# head = reverseLL2(head)
# printLL(head)

# Itretive solution of the reverse list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverseLL(head):
    prev = None
    next_node = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    newHead = prev
    return newHead


def printLL(head):
    while head is not None:
        print(str(head.data)+"->", end="")
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
head = reverseLL(head)
printLL(head)



