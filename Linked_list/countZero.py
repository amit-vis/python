# # # count zero code
# # # def countZero(n):
# # #     if n<10:
# # #         if n==0:
# # #             return 1
# # #         else:
# # #             return 0
# # #     if n%10==0:
# # #         return 1+countZero(n//10)
# # #     else:
# # #         return countZero(n//10)
    
# # # n = int(input("Enter the number: "))
# # # ans = countZero(n)
# # # print(ans)

# # class Node:
# #     def __init__(self,value):
# #         self.a = value
# #         self.next = None

# # # n1 = Node(2)
# # # n2 = Node(6)
# # # n3 = Node(7)
# # # n4 = Node(3)
# # # n5 = Node(4)

# # # n1.next = n2
# # # n2.next = n3
# # # n3.next = n4
# # # n4.next = n5

# # # temp = n1
# # # while temp != None:
# # #     print(temp.a, end=' ')
# # #     temp = temp.next

# # # Delete Node function

# # def deleteNode(head):
# #     if head == None:
# #         return
# #     if head.next ==None:
# #         head = None
# #         return
# #     temp = head
# #     while temp.next.next != None:
# #         print(temp.a)
# #         temp = temp.next
# #     p = temp.next
# #     temp.next = None
# #     del p

# # n1 = Node(2)
# # n2 = Node(6)
# # n3 = Node(7)
# # n4 = Node(3)
# # n5 = Node(4)

# # n1.next = n2
# # n2.next = n3
# # n3.next = n4
# # n4.next = n5

# # deleteNode(n1)
# # temp = n1
# # while temp != None:
# #     print(temp.a, end=' ')
# #     temp = temp.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# def printLL(head):
#     while head is not None:
#         print(str(head.data) + '->', end="")
#         head = head.next
#     print(None)
#     return

# # take input code
# def takeInput():
#     inputList = [int(ele) for ele in input().split()]
#     head = None
#     for currData in inputList:
#         if currData == -1:
#             break
#         newNode = Node(currData)
#         if head is None:
#             head = newNode
#         else:
#             curr = head
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = newNode
#     return head

# head = takeInput()
# printLL(head)
# def printLL(head):
#     while head is not None:
#         print(str(head.data)+ '->',end="")
#         head = head.next
#     print(None)
#     return

# def takeInput():
#     linkList = [int(ele) for ele in input().split()]
#     head = None
#     for currList in linkList:
#         if currList == -1:
#             break
#         newNode = Node(currList)
#         if head is None:
#             head = newNode
#         else:
#             curr =head
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = newNode

#     return head
# head = takeInput()
# printLL(head)

def printLL(head):
    while head is not None:
        print(str(head.data)+'->', end="")
        head = head.next
    print(None)
    return

def takeInput():
    linkList = [int(ele) for ele in input().split()]
    head = None
    for currData in linkList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

head = takeInput()
printLL(head)