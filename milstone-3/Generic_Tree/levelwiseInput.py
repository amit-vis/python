import queue
class NodeTree:
    def __init__(self,data):
        self.data = data
        self.children = []

def printTree(root):
    if root == None:
        return
    print(root.data, ':', end='')
    for child in root.children:
        print(child.data, ',', end='')
    print()
    for child in root.children:
        printTree(child)

def takeInputLevel():
    q=queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = NodeTree(rootData)
    q.put(root)
    while not q.empty():
        current_Node = q.get()
        print("Enter the number of child", current_Node.data)
        numchildren = int(input())
        for i in range(numchildren):
            print("Enter the next child")
            childData = int(input())
            child = NodeTree(childData)
            current_Node.children.append(child)
            q.put(child)
    return root

root = takeInputLevel()
printTree(root)