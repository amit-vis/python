import queue
class BinaryNodeTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findPath(root, data):
    if root == None:
        return []
    if root.data == data:
        return [root.data]
    if root.data>data:
        lst = findPath(root.left, data)
        if lst != []:
            lst.append(root.data)
    if root.data<data:
        lst = findPath(root.right, data)
        if lst != []:
            lst.append(root.data)
    return lst

def printTree(root):
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print("L", root.left.data, end=',')
    if root.right != None:
        print('R', root.right.data)
    print()
    printTree(root.left)
    printTree(root.right)

def takeInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryNodeTree(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the left data", current_node.data)
        leftRootData = int(input())
        if leftRootData != -1:
            leftChild = BinaryNodeTree(leftRootData)
            current_node.left = leftChild
            q.put(leftChild)
        
        print("Enter right child Data", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryNodeTree(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInput()
printTree(root)
root = findPath(root, 5)
print(root)