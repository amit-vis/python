class TreeNodes:
    def __init__(self,data):
        self.data = data
        self.children = []

def sumOfNode(root):
    if root == None:
        return 0
    sumNode = root.data
    for child in root.children:
        sumNode += sumOfNode(child)
    return sumNode

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
    print("Enter a root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNodes(rootData)
    print("Enter the number of children")
    children = int(input())
    for i in range(children):
        child = takeInput()
        root.children.append(child)
    return root

root = takeInput()
printTree(root)
print(sumOfNode(root))