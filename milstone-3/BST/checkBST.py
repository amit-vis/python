import queue
class BinaryNodeTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# def minTree(root):
#     if root == None:
#         return 1767462785
#     leftMin = minTree(root.left)
#     rightMin = minTree(root.right)
#     return min(leftMin, rightMin, root.data)
# def maxTree(root):
#     if root == None:
#         return -4353462
#     leftMax = maxTree(root.left)
#     rightMax = maxTree(root.right)
#     return max(leftMax,rightMax,root.data)
# def checkBST(root):
#     if root == None:
#         return True
#     leftMax = maxTree(root.left)
#     rightMin = minTree(root.right)
#     if root.data <= leftMax or root.data>rightMin:
#         return False
#     else:
#         return checkBST(root.left) and checkBST(root.right)

# def isBST2(root):
#     if root == None:
#         return 100000, -100000, True
#     leftMin, leftMax, isLeftBST = isBST2(root.left)
#     rightMin, rightMax, isRightBST = isBST2(root.right)

#     minimum = min(leftMin, rightMin, root.data)
#     maximum = max(leftMax, rightMax, root.data)
#     isTreeBST = True
#     if root.data <= leftMax or root.data> rightMin:
#         isTreeBST = False
#     if not(isLeftBST) or not(isRightBST):
#         isTreeBST = False
#     return minimum, maximum, isTreeBST
def isBST3(root, min_range, max_range):
    if root == None:
        return True
    if root.data <min_range or root.data>max_range:
        return False
    
    isLeftWith = isBST3(root.left, min_range, root.data -1)
    isRightWith = isBST3(root.right, root.data, max_range)

    return isLeftWith and isRightWith

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
print(isBST3(root, -100000, 1000000))