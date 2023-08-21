import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def helper(root):
    if root is None:
        return None, 0
    NodeData = root
    sumOfRoot = root.data
    for child in root.children:
        childNode, sumOfNode = helper(child)
        if sumOfRoot < sumOfNode:
            NodeData = childNode
            sumOfRoot = sumOfNode
    return NodeData, sumOfRoot

def maxNode(root):
    node = helper(root)
    return node


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
print(maxNode(root))
