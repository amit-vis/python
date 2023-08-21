import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def containX(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    for child in root.children:
        isPresent = containX(child,x)
        if isPresent:
            return True
    return False

def printTree(root):
    if root == None:
        return
    print(root.data, ":", end='')
    for child in root.children:
        print(child.data, ',', end='')
    print()
    for child in root.children:
        printTree(child)

def takeInput():
    q= queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the number of children", current_node.data)
        numchildren = int(input())
        for i in range(numchildren):
            print("Enter the next child")
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root

root = takeInput()
printTree(root)
x = int(input("Enter the value of x: "))
print(containX(root, x))
