class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def ithList(head,i):
    count = 0
    curr = head
    if curr == None:
        return
    while count<i and curr != None:
        count +=1
        curr = curr.next
    return curr.data
def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end='')
        head = head.next
    print(None)
    return

def takeInput():
    inputLinkList = [int(x) for x in input().split()]
    head = None
    tail = None
    for currData in inputLinkList:
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
i = int(input("enter the number"))
print(ithList(head,i))