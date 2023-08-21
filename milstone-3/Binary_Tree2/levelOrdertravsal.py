import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelTravsal(root):
    curr_level = [root]
    while curr_level != []:
        new_level = []
        for node in curr_level:
            if node.left != None:
                new_level.append(node.left)
            if node.right != None:
                new_level.append(node.right)
        for node in curr_level:
            print(node.data, end=' ')
        print()
        curr_level = new_level

def printTree(root):
    if root == None:
        return
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data, end=":")
        if current_node.left != None:
            print("L", end='')
            print(current_node.left.data, end=",")
            q.put(current_node.left)
        if current_node.right != None:
            print("R", end='')
            print(current_node.right.data, end=",")
            q.put(current_node.right)
        print()

def takInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left data of the root", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter the right data of the root", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root

root = takInput()
levelTravsal(root)