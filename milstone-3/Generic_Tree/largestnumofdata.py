class treeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

# def largestNumNode(root):
#     if root == None:
#         return None
#     maxData = root
#     for child in root.children:
#         maxChild = largestNumNode(child)
#         if maxChild and maxChild.data> maxData.data:
#             maxData = maxChild
#     return maxData

# Height of tree
# def Height(root):
#     if root is None:
#         return 0
#     maxChildHeight = 0
#     for child in root.children:
#         HeightofTree = Height(child)
#         maxChildHeight = max(maxChildHeight, HeightofTree)
#     return 1 + maxChildHeight

def Height(root):
    if root is None:
        return 0
    maxChildHeight = 0
    for child in root.children:
        childHeight = Height(child)
        maxChildHeight = max(maxChildHeight, childHeight)
    return 1 + maxChildHeight
 
def printTree(root):

    if root == None:
        return
    print(root.data, ':', end='')
    for child in root.children:
        print(child.data, ',', end='')
    print()
    for child in root.children:
        printTree(child)


def takeInput():
    print("Enter the root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = treeNode(rootData)
    print("Enter the number of children")
    children = int(input())
    for i in range(children):
        child = takeInput()
        root.children.append(child)
    return root

root = takeInput()
printTree(root)
largestData = Height(root)
print(largestData)
