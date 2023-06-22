class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def length(head):
    count = 0
    while head:
        count +=1
        head = head.next
    return count
   
def deleteNode(head, pos):
    if pos < 0 or pos >= length(head):
        return head

    if pos == 0:
        return head.next

    count = 0
    prev = None
    curr = head
    while count < pos:
        prev = curr
        curr = curr.next
        count += 1

    newNode = curr.next
    prev.next = newNode
    del curr
    return head

def printLL(head):
    while head is not None:
        print(str(head.data) + "->",end='')
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
pos = int(input("Enter the data here: "))
head = deleteNode(head, pos)
printLL(head)