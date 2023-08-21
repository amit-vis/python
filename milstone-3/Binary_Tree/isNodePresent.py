class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodeIsPresent(root, k):
    if root == None:
        return False
    if root.data == k:
        return True
    return nodeIsPresent(root.left,k) or nodeIsPresent(root.right, k)
    

def printData(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L", root.left.data, end=",")
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
k = int(input("value of k"))
print(nodeIsPresent(root, k))