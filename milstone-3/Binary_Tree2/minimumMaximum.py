import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def maximumMinimum(root):
    if root == None:
        return 6721354568, -76526135462362
    leftmin,leftmax = maximumMinimum(root.left)
    rightmin, rightmax = maximumMinimum(root.right)

    minimumData = min(root.data,leftmin, rightmin)
    maximumData = max(root.data,leftmax, rightmax)
    return minimumData, maximumData

def printTree(root):
    if root == None:
        return
    q= queue.Queue()
    q.put(root)
    while (not(q.empty())):
        currentNode = q.get()
        print(currentNode.data, end=",")
        if currentNode.left != None:
            print("L:", end='')
            print(currentNode.left.data, end=":")
            q.put(currentNode.left)
        if currentNode.right != None:
            print('R:', end='')
            print(currentNode.right.data, end=',')
            q.put(currentNode.right)
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
        current_node = q.get()
        print("Enter the left of root", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter the right data of root", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)

print(maximumMinimum(root))