# def buubleSort(arr):
#     for i in range(len(arr)):
#         for j in range(0,len(arr)-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr

# arr = [int(x) for x in input().split()]
# print(buubleSort(arr))

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def bubbleSort(head):
    # if head is None:
    #     return 
    # sorted_data = head
    # while sorted_data.next:
    #     current = sorted_data.next
    #     if current.data < sorted_data.data:
    #         sorted_data.next = current.next
    #         current.next = head
    #         head =current
    #     else:
    #         prev = sorted_data
    #         while current.data>=sorted_data.next.data and sorted_data.next != current:
    #             sorted_data = sorted_data.next
    #         prev.next = current.next
    #         current.next = sorted_data.next
    #         sorted_data.next = current
    # return head 
    if head is None or head.next is None:
        return head
    length = 0
    current = head
    while current:
        length +=1
        current = current.next

    for i in range(length):
        prev = None
        current = head
        new_node = current.next

        for j in range(length-i-1):
            if current.data > new_node.data:
                if prev is not None:
                    prev.next = new_node
                else:
                    head = new_node
                current.next = new_node.next
                new_node.next = current
                prev = new_node
                new_node = current.next
            else:
                prev = current
                current = new_node
                new_node = current.next if current else None
    return head
        

def printLL(head):
    while head is not None:
        print(str(head.data)+'->', end="")
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
head = bubbleSort(head)
printLL(head)