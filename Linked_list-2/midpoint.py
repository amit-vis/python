class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def midPoint(head):
    slow = head
    fast = head
    if head != None:
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

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
midPoint = midPoint(head)
print(midPoint)