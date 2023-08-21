import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertDuplicate(root):
    if root == None:
        return
    insertDuplicate(root.left)
    insertDuplicate(root.right)
    oldLeft = root.left
    root.left = BinaryTreeNode(root.data)
    root.left.left = oldLeft
    return root

def printTree(root):
    if  root == None:
        return
    q = queue.Queue()
    q.put(root)
    while (not(q.empty())):
        current_node = q.get()
        print(current_node.data, end=':')
        if current_node.left != None:
            print("L:", end='')
            print(current_node.left.data, end=",")
            q.put(current_node.left)

        if current_node.right != None:
            print("R:", end='')
            print(current_node.right.data, end=",")
            q.put(current_node.right)
        print()

def takeInput():
    q = queue.Queue()
    print("Enter Root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_Node = q.get()
        print("Enter the left child data of root", current_Node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_Node.left = leftChild
            q.put(leftChild)
        print("Enter the right child data of root", current_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_Node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)
root = insertDuplicate(root)
printTree(root)