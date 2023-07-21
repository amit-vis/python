class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printData(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print('L', root.left.data, end=",")
    if root.right != None:
        print('R', root.right.data)
    print()
    printData(root.left)
    printData(root.right)

# btn1 = BinaryTreeNode(1)
# btn2 = BinaryTreeNode(2)
# btn3 = BinaryTreeNode(6)
# btn4 = BinaryTreeNode(7)
# btn5 = BinaryTreeNode(8)


# btn1.left = btn2
# btn1.right = btn3
# btn2.left = btn4
# btn2.right = btn5

# printData(btn1)

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
