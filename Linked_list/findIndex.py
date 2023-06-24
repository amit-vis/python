class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# def findIndex(head, index):
#     if head == None:
#         return -1
#     curr = head
#     count = 0
#     while curr != None and curr.data != index:
#         curr = curr.next
#         count +=1
#     if curr != None:
#         return count
#     else:
#         return -1
def findIndex(head, index, count=0):
    if head is None:
        return -1
    if head.data == index:
        return count
    else:
        return findIndex(head.next, index, count+1)
    

def printLL(head):
    while head is not None:
        print(str(head.data)+'->', end='')
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
    
head = takeInput()
printLL(head)
index = int(input("Enter the index: "))
count = findIndex(head, index)
if count == -1:
    print("Index not found")
else:
    print("Index found at position:", count)
