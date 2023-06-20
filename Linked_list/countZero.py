# count zero code
# def countZero(n):
#     if n<10:
#         if n==0:
#             return 1
#         else:
#             return 0
#     if n%10==0:
#         return 1+countZero(n//10)
#     else:
#         return countZero(n//10)
    
# n = int(input("Enter the number: "))
# ans = countZero(n)
# print(ans)

class Node:
    def __init__(self,value):
        self.a = value
        self.next = None

# n1 = Node(2)
# n2 = Node(6)
# n3 = Node(7)
# n4 = Node(3)
# n5 = Node(4)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# temp = n1
# while temp != None:
#     print(temp.a, end=' ')
#     temp = temp.next

# Delete Node function

def deleteNode(head):
    if head == None:
        return
    if head.next ==None:
        head = None
        return
    temp = head
    while temp.next.next != None:
        print(temp.a)
        temp = temp.next
    p = temp.next
    temp.next = None
    del p

n1 = Node(2)
n2 = Node(6)
n3 = Node(7)
n4 = Node(3)
n5 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

deleteNode(n1)
temp = n1
while temp != None:
    print(temp.a, end=' ')
    temp = temp.next
