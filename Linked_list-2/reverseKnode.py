class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def reverseK(head, k):
    if head is None:
        return None
    current = head
    next_node = None
    prev_node = None
    count = 0

    while current and count <k:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
        count += 1
    if next_node is not None:
        head.next = reverseK(next_node, k)
    return prev_node

def printLL(head):
    while head is not None:
        print(str(head.data) + '->', end='')
        head = head.next
    print(None)
    return

def takInput():
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

head = takInput()
printLL(head)
k = int(input("enter the number: "))
head = reverseK(head,k)
printLL(head)