import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def structurcally(root1, root2):
    if root1 == None:
        if root2 == None:
            return True
        return False
    if (root1.data != root2.data) or (len(root1.children) != len(root2.children)):
        return False
    for child1, child2 in zip(root1.children, root2.children):
        if not structurcally(child1, child2):
            return False
    return True



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

root1 = takeInput()
printTree(root1)

root2 = takeInput()
printTree(root2)
print(structurcally(root1, root2))
