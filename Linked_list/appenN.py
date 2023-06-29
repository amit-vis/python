class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def appendNth(head, N):
    if N == 0 or not head:
        return head
    length = 0
    curr = head
    while curr:
        curr = curr.next
        length +=1
    
    if N>=length:
        return head
    
    split_position = length - N

    curr = head
    prev = None
    while split_position>0:
        prev = curr
        curr = curr.next
        split_position -= 1
    newNode = curr
    curr = newNode
    while curr.next:
        curr = curr.next
    curr.next = head
    prev.next = None
    return newNode

def printLL(head):
    while head is not None:
        print(str(head.data) + '->',end="")
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
N= int(input("Enter the number: "))
head = appendNth(head, N)
printLL(head)