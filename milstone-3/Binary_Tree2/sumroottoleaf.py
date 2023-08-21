import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# def findPathSum(root, k):
#     current_sum = []
#     printSumOfk(root, k,current_sum)
#     for i in current_sum:
#         print(i, end=' ')

# def printSumOfk(root, k, current_sum):
#     if root == None:
#         return
#     k += root.data
#     if root.left == None and root.right == None:
#         current_sum.append(k)
#         return []
#     if root.left != None:
#         printSumOfk(root.left, k, current_sum)
#     else:
#         printSumOfk(root.right, k, current_sum)

def findSumPath(root, k, current_sum =[]):
    if root == None:
        return
    current_sum.append(root.data)
    if not root.left and not root.right and sum(current_sum) == k:
        print(current_sum)
    findSumPath(root.left, k, current_sum.copy())
    findSumPath(root.right, k, current_sum.copy())

def printTree(root):
    if root == None:
        return
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        current_Node = q.get()
        print(current_Node.data, end=":")
        if current_Node.left != None:
            print("L:", end="")
            print(current_Node.left.data, end=',')
            q.put(current_Node.left)
        if current_Node.right != None:
            print("R:", end='')
            print(current_Node.right.data)
            q.put(current_Node.right)
        print()

def takeInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("enter the left data of root", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("enter the right child of data", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)
k = int(input())
findSumPath(root, k)