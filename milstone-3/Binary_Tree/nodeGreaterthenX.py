class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodeGreaterthenX(root,x):
    if root == None:
        return 0
    leftCount = nodeGreaterthenX(root.left,x)
    rightCount = nodeGreaterthenX(root.right, x)
    total_count = leftCount + rightCount
    if root.data>x:
        return total_count + 1
    else:
        return total_count

def printData(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data)
    printData(root.left)
    printData(root.right)
    return root

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
printData(root)
x = int(input("Enter the X: "))
print(nodeGreaterthenX(root, x))