import queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

def DepthOfTree(root, d=0):
    if root == None:
        return 0
    root.d = d
    for child in root.children:
        DepthOfTree(child, d+1)
def actualDepthOfTree(root):
    DepthOfTree(root, 0)
    
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
actualDepthOfTree(root)
printTree(root) 
