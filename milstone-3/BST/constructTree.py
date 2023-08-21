import queue
class BinaryNodeTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(root, arr):
    if not arr:
        return None
    mid = len(arr)//2
    root = BinaryNodeTree(arr[mid])
    leftTree = constructTree(root.left, arr[:mid])
    rightTree = constructTree(root.right, arr[mid+1:])
    root.left = leftTree
    root.right = rightTree
    return root

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
arr = [int(x) for x in input().split()]
printTree(root)