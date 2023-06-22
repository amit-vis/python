# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def lengthLL(head):
#     count = 0
#     while head:
#         count +=1
#         head = head.next
#     return count

# def printLL(head):
#     while head is not None:
#         print(str(head.data) + "->", end='')
#         head = head.next
#     print(None)
#     return    
# def takeInput():
#     inputList = [int(x) for x in input().split()]
#     head = None
#     tail = None
#     for currData in inputList:
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
# print(lengthLL(head))

# recursive lengthLL
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def lengthLLRecur(head):
    if not head:
        return 0
    else:
        return 1+lengthLLRecur(head.next)
def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
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
print(lengthLLRecur(head))