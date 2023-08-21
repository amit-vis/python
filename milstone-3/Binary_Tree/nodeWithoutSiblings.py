class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def nodeWithoutSiblings(root):
    if root == None:
        return
    if root.left != None and root.right != None:
        nodeWithoutSiblings(root.left)
        nodeWithoutSiblings(root.right)
    if root.left != None:
        print(root.left.data, end="")
        nodeWithoutSiblings(root.left)

    if root.right != None:
        print(root.right.data, end=' ')
        nodeWithoutSiblings(root.right)

def printData(root):
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print("L",root.left.data, end=',')
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
nodeWithoutSiblings(root)