class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverseLL(head):
    if head:
        reverseLL(head.next)
        print(head.data, end=' ')
    else:
        return 

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
head = reverseLL(head)
printLL(head)
