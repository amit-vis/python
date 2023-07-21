class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def replacewithdepth(root, d=0):
    if root == None:
        return
    if root.data != None:
        root.data = d

    replacewithdepth(root.left, d+1)
    replacewithdepth(root.right, d+1)

def printData(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print('L', root.left.data, end=',')
    if root.right != None:
        print('R', root.right.data)

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
replacewithdepth(root)
printData(root)