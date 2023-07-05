# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def mergeLink(head1, head2):
#     fh = None
#     ft = None
#     if head1.data>head2.data:
#         fh = head2
#         ft = head2
#         head1 = head1.next

#     else:
#         fh = head1
#         ft = head1
#         head2 = head2.next

#     while head1 != None and head2 != None:
#         if head1.data > head2.data:
#             ft.next = head2
#             ft = ft.next
#             head2 = head2.next
#         else:
#             ft.next = head1
#             ft = ft.next
#             head1 = head1.next
#     if head1 != None:
#         ft.next = head1

#     if head2 != None:
#         ft.next = head2
       
#     return fh

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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLink(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data < head2.data:
        fh = head1
        ft = head1
        head1 = head1.next
    else:
        fh = head2
        ft = head2
        head2 = head2.next

    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            ft.next = head1
            ft = ft.next
            head1 = head1.next
        else:
            ft.next = head2
            ft = ft.next
            head2 = head2.next

    if head1 is not None:
        ft.next = head1
    if head2 is not None:
        ft.next = head2

    return fh

def printLL(head):
    while head is not None:
        print(str(head.data) + '->', end='')
        head = head.next
    print(None)

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

print("Enter the elements of the first linked list:")
head1 = takeInput()

print("Enter the elements of the second linked list:")
head2 = takeInput()

merged_head = mergeLink(head1, head2)

print("Merged Linked List:")
printLL(merged_head)