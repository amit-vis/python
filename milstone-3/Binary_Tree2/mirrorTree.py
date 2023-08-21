class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirrorTree(root):
    if root == None:
        return None
    temp = root
    mirrorTree(root.left)
    mirrorTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp
    return root

def printData(root):
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print('L', root.left.data, end=",")
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
print("+++++++++++++")
root = mirrorTree(root)
printData(root)