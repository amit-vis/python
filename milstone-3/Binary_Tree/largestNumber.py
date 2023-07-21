class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def largestData(root):
    if root == None:
        return -664567678
    leftNumber = largestData(root.left)
    rightNumber = largestData(root.right)
    return max(leftNumber,rightNumber,root.data)
    

def printRoot(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end="")
    if root.right != None:
        print("R", root.right.data, end="")
    print()
    printRoot(root.left)
    printRoot(root.right)

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryNode(rootData)
    leftData = takeInput()
    rightData = takeInput()
    root.left = leftData
    root.right = rightData
    return root

root = takeInput()
printRoot(root)
print(largestData(root))