class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def numNodes(root):
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count


def printTree(root):
    if root == None:
        return
    print(root.data,':', end='')
    for child in root.children:
        print(child.data,',', end='')
    print()
    for child in root.children:
        printTree(child)

def takeInput():
    print("Enter the root")
    rootData = int(input())
    root = treeNode(rootData)
    print("Enter the number of children")
    if rootData == -1:
        return None
    children = int(input())
    for i in range(children):
        child = takeInput()
        root.children.append(child)
    return root


root = takeInput()
printTree(root)
print(numNodes(root))