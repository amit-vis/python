class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# def numberOfNodes(root):
#     if root == None:
#         return 0
#     leftCount = numberOfNodes(root.left)
#     rightCount  = numberOfNodes(root.right)
#     return 1+ leftCount+rightCount
def sumOfNodes(root):
    if root == None:
        return 0
    leftSum = sumOfNodes(root.left)
    rightSum = sumOfNodes(root.right)
    return root.data +leftSum+rightSum

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
    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
printRoot(root)
print(sumOfNodes(root))
