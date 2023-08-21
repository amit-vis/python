import queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

def countOfLeaf(root):
    if root == None:
        return 0
    if not root.children:
        return 1
    count = 0
    for child in root.children:
        count += countOfLeaf(child)
    return count

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
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the number of child", current_node.data)
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
print(countOfLeaf(root))