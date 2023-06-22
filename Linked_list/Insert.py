# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def length(head):
#     count = 0
#     while head:
#         count +=1
#         head.next
#     return count

# def inserIth(head, data,i):
#     if i<0 or i>length(head):
#         return head
#     count = 0
#     prev = None
#     curr = head
#     while count<i:
#         prev = curr
#         curr = curr.next
#         count +=1
#     newNode = Node(data)
#     if head is not None:
#         prev.next = newNode
#     else:
#         head = newNode
#     newNode.next = curr
#     return head

# def printLL(head):
#     while head is not None:
#         print(str(head.data)+ '->', end='')
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
# head = inserIth(head, 3, 2)
# print(printLL(head))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def inserIth(head, data, i):
    if i < 0 or i > length(head):
        return head
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) + '->', end='')
        head = head.next
    print(None)
    return

def takeInput():
    linkList = [int(x) for x in input().split()]  # Example input, replace with your own list
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
data = int(input("Enter the data here: "))
i = int(input("Enter the i number: "))
head = inserIth(head, data, i)
printLL(head)
