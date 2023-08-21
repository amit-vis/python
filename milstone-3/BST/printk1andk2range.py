import queue
class BinaryNodeTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printRange(root, k1, k2):
    if root == None:
        return
    if root.data >k2:
        printRange(root.left, k1,k2)
    if root.data < k1:
        printRange(root.right, k1, k2)
    else:
        printRange(root.left, k1, k2)
        print(root.data)
        printRange(root.right, k1, k2)

def printTree(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L:",root.left.data, end=",")
    if root.right != None:
        print("R:", root.right.data)
    print()
    printTree(root.left)
    printTree(root.right)

def takeInput():
    q = queue.Queue()
    print("Enter Root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryNodeTree(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left child data", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryNodeTree(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter the right Child", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryNodeTree(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)
k1 = int(input("Enter k1"))
k2 = int(input("Enter k2"))
printRange(root, k1, k2)