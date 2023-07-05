class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swapNode(head, i, j):
    if i == j:
        return
    p1 = None
    c1 = head
    while c1 and c1.data != i:
        p1 = c1
        c1 = c1.next
    p2 = None
    c2 = head
    while c2 and c2.data != j:
        p2 = c2
        c2 = c2.next
    if c1 == None or c2 == None:
        return
    if p1 != None:
        p1.next = c2
    else:
        head = c2
    if p2 != None:
        p2.next = c1
    else:
        head = c1
    temp = c2.next
    c2.next = c1.next
    c1.next = temp
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) + '->',end="")
        head = head.next
    print(None)
    return

def takInput():
    linkList = [int(x) for x in input().split()]
    head = None
    tail = None
    for currData in linkList:
        if currData ==-1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

head = takInput()
printLL(head)
i = int(input("Enter the i: "))
j = int(input("Enter the j: "))
swapData = swapNode(head, i , j)
printLL(swapData)