class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLL(head):
    if head == None:
        return head
    if head.next == None:
        return head
    smallHead = reverseLL(head.next)
    head.next.next = head
    head.next = None
    return smallHead

# def nextNumber(head):
#     head = reverseLL(head)
#     f= True
#     curr = head
#     while curr is not None and f==True:
#         if(curr.next==None and curr.data == 9):
#             curr.data = 1
#             tamp = Node(0)
#             tamp.next = head
#             head = tamp
#             curr = curr.next
#         elif (curr.data == 9):
#             curr.data = 0
#             curr = curr.next
#         else:
#             curr.data = curr.data+1
#             curr = curr.next
#             f=False
#     head = reverseLL(head)
#     return head

def addOne(head):
    if head is None:
        return None
    head = reverseLL(head)
    curr = head
    carry = 1
    while carry:
        curr.data += 1
        if(curr.data<10):
            return reverseLL(head)
        else:
            curr.data = 0
        if (curr.next == None):
            break
        else:
            curr = curr.next
    curr.next = Node(1)
    return reverseLL(head)

def printLL(head):
    while head is not None:
        print(str(head.data)+'->',end='')
        head = head.next
    print(None)
    return

def takInput():
    linkList = [int(x) for x in input().split()]
    head = None
    tail = None
    for currDate in linkList:
        if currDate == -1:
            break
        newNode = Node(currDate)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

head = takInput()
printLL(head)
headreve = addOne(head)
printLL(headreve)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    if not head or not head.next:
        return head

    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def nextNumber(head):
    if not head:
        return None
    
    reversed_head = reverseList(head)
    
    current = reversed_head
    carry = 1
    
    while current:
        sum = current.data + carry
        if sum <= 9:
            current.data = sum
            carry = 0
        else:
            current.data = 0
            carry = 1
        current = current.next
    
    updated_head = reverseList(reversed_head)
    if carry == 1:
        new_head = Node(1)
        new_head.next = updated_head
        updated_head = new_head
    
    return updated_head
        
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)