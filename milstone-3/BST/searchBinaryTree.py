import queue
class BinaryNodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def searchNode(root, x):
    if root == None:
        return False
    if root.data == x:
        return True
    if root.data <= x:
        return searchNode(root.right, x)
    else:
        return searchNode(root.left, x)

def printTree(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_Node = q.get()
        print(current_Node.data, end=":")
        if current_Node.left != None:
            print("L:", end='')
            print(current_Node.left.data, end=",")
            q.put(current_Node.left)
        if current_Node.right != None:
            print("R:", end='')
            print(current_Node.right.data, end=',')
            q.put(current_Node.right)
        print()

def takeInput():
    q = queue.Queue()
    print("Enter the Root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryNodeTree(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left child Data", current_node.data)
        leftchildData = int(input())
        if leftchildData != -1:
            leftChild = BinaryNodeTree(leftchildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter the right child data", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryNodeTree(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)
x = int(input("Enter the x here: "))
print(searchNode(root, x))