# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def mergeSort(head):
#     if head is None or head.next is None:
#         return head
#     mid = findMiddle(head)
#     head2 = mid.next
#     mid.next = None
#     head = mergeSort(head)
#     head2 = mergeSort(head2)
#     return merge(head, head2)

# def findMiddle(head):
#     slow = head
#     fast = head
#     while fast.next is not None and fast.next.next is not None:
#         slow = slow.next
#         fast = fast.next.next
#     return slow

# def merge(head1, head2):
#     if head1 is None:
#         return head2
#     if head2 is None:
#         return head1
#     if head1.data < head2.data:
#         fh = head1
#         ft = head1
#         head1 = head1.next
#     else:
#         fh = head2
#         ft = head2
#         head2 = head2.next
#     while head1 is not None and head2 is not None:
#         if head1.data < head2.data:
#             ft.next = head1
#             ft = ft.next
#             head1 = head1.next
#         else:
#             ft.next = head2
#             ft = ft.next
#             head2 = head2.next
#     if head1 is not None:
#         ft.next = head1
#     if head2 is not None:
#         ft.next = head2
#     return fh

# def printLL(head):
#     while head is not None:
#         print(str(head.data) + '->', end="")
#         head = head.next
#     print(None)

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
# findMerge = mergeSort(head)
# printLL(findMerge)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSort(head):
    if head is None or head.next is None:
        return head
    mid = midPoint(head)
    head2 = mid.next
    mid.next = None
    head = mergeSort(head)
    head2 = mergeSort(head2)
    return merge(head, head2)

def midPoint(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <head2.data:
        Fh = head1
        Ft = head1
        head1 = head1.next
    else:
        Fh = head2
        Ft = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            Ft.next = head1
            Ft = Ft.next
            head1 = head1.next
        else:
            Ft.next = head2
            Ft = Ft.next
            head2 = head2.next
    if head1 is not None:
        Ft.next = head1
    if head2 is not None:
        Ft.next = head2
    return Fh

def printLL(head):
    while head is not None:
        print(str(head.data) + '->', end="")
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
findMerge = mergeSort(head)
printLL(findMerge)