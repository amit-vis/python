class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):
    if root == None:
        return
    print(root.data, end=':')
    for child in root.children:
        printTree(child)
    print()

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,':',end='')
    for child in root.children:
        print(child.data, ',', end='')
    
    print()

    for child in root.children:
        printTreeDetailed(child)

def takeInput():
    print("Enter the root")
    rootData = int(input())
    root = Treenode(rootData)
    print("Enter the number of children count", rootData)
    childrenCount = int(input())
    if rootData == -1:
        return None
    for i in range(childrenCount):
        child = takeInput()
        root.children.append(child)
    return root

root = takeInput()
printTreeDetailed(root)