class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# preorder
def preorder(root):
    if root == None:
        return 0
    print(root.data)
    preorder(root.left)
    preorder(root.right)

# postorder
def postorder(root):
    if root == None:
        return 0
    postorder(root.left)
    postorder(root.right)
    print(root.data)

# inorder
def inorder(root):
    if root == None:
        return 0
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def printData(root):
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print("L", root.left.data, end="")
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
    letfTree = takeInput()
    rightTree = takeInput()
    root.left = letfTree
    root.right = rightTree
    return root

root = takeInput()
printData(root)
inorder(root)