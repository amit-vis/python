class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def deleteAlternate(head):
    if head is None:
        return head
    curr = head
    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next
    return head

def printLL(head):
    while head is not None:
        print(str(head.data)+'->', end="")
        head = head.next
    print(None)
    return

def takeInput():
    linklist = list(map(int, input().split()))
    head = None
    tail = None
    for currData in linklist:
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

item = deleteAlternate(head)
printLL(item)