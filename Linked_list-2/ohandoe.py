# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def oddEven(head):
#     OH = None
#     OT = None
#     EH = None
#     ET = None
#     if head is None:
#         return head
#     while head is not None:
#         if head.data % 2==0:
#             if EH is None:
#                 EH = head
#                 ET = head
#             else:
#                 ET.next = head
#                 ET = ET.next
#         else:
#             if OH is None:
#                 OH = head
#                 OT = head
#             else:
#                 OT.next = head
#                 OT = OT.next
#         head = head.next
#     if OH is not None:
#         OT.next = EH
#     else:
#         return EH
#     if EH is not None:
#         ET.next = None
#     return OH

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
# head = oddEven(head)
# printLL(head)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def oddEvensap(head):
    if head is None:
        return head
    EH = None
    ET = None
    OT = None
    OH = None
    while head is not None:
        if head.data%2 == 0:
            if EH is None:
                EH = head
                ET = head
            else:
                ET.next = head
                ET = ET.next
        else:
            if OH is None:
                OH = head
                OT = head
            else:
                OT.next = head
                OT = OT.next
        head = head.next
    if OH is not None:
        OT.next = EH
    else:
        return EH
    if EH is not None:
        ET.next = None
    return OH

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
head = oddEvensap(head)
printLL(head)
