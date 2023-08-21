import queue
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depthofRoot(root, k):
    if root == None:
        return 0
    if k == 0:
        print(root.data)
        return
    depthofRoot(root.left, k-1)
    depthofRoot(root.right, k-1)

def distanceOfroot(root,node,k):
    if root is None or node is None or k<1:
        return -1
    if root.data == node:
        depthofRoot(root,k)
        return 0
    lt = distanceOfroot(root.left, node, k)
    if lt != -1:
        if lt+1 == k:
            print(root.data)
        else:
            depthofRoot(root.right, k-(lt+2))
        return lt+1
    rt = distanceOfroot(root.right, node, k)
    if rt != -1:
        if rt+1 == k:
            print(root.data)
        else:
            depthofRoot(root.left, k-(rt+2))
        return rt+1
    return -1
    
def printTree(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print(current_node.data, end=":")
        if current_node.left != None:
            print("L:", end='')
            print(current_node.left.data, end=',')
            q.put(current_node.left)
        if current_node.right != None:
            print("R:", end='')
            print(current_node.right.data)
            q.put(current_node.right)
        print()

def takeInput():
    q = queue.Queue()
    print("Enter the root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left data of root", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = Node(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter the right data of root", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = Node(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)
node = int(input("Enter the node: "))
k = int(input("Enter the k: "))
distanceOfroot(root,node, k)