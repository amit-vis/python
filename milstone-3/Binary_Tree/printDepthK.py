class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# def printDepthK(root, k):
#     if root == None:
#         return
#     if k == 0:
#         print(root.data)
#         return
#     printDepthK(root.left, k-1)
#     printDepthK(root.right, k-1)

# anotherApproach

def printAtk(root, k, d=0):
    if root == None:
        return
    if k == d:
        print(root.data)
        return
    printAtk(root.left, k, d+1)
    printAtk(root.right, k,d+1)

def printData(root):
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print("L", root.left.data, end=',')
    if root.right != None:
        print("R", root.right.data)
    print()
    printData(root.left)
    printData(root.right)

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
printData(root)
k = int(input("Enter the K: "))
print(printAtk(root, k))