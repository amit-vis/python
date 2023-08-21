import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# def printData(root):
#     if root == None:
#         return
#     print(root.data, end=':')
#     if root.left != None:
#         print('L', root.left.data, end=',')
#     if root.right != None:
#         print('R', root.right.data)
#     print()
#     printData(root.left)
#     printData(root.right)
def printData(root):
    if root == None:
        return
    q = queue.Queue()
    q.put(root)
    while (not(q.empty())):
        current_node = q.get()
        print(current_node.data, end=':')
        if current_node.left != None:
            print('L:', end='')
            print(current_node.left.data, end=',')
            q.put(current_node.left)
        else:
            print('L:-1', end=',')
        if current_node.right != None:
            print('R:', end='')
            print(current_node.right.data, end=',')
            q.put(current_node.right)
        else:
            print('R:-1', end=',')
        print()



def takeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node = q.get()
        print("Enter the left child of data", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)
        print("Enter the right child of data", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)
    return root

root = takeInputLevelWise()
printData(root)