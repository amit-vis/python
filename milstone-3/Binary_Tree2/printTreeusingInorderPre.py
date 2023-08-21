import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# def printData(root):
#     if root == None:
#         return
#     q = queue.Queue()
#     q.put(root)
#     while (not(q.empty())):
#         currente_node = q.get()
#         print(currente_node.data, end=":")
#         if currente_node.left != None:
#             print('L:', end='')
#             print(currente_node.left.data, end=',')
#             q.put(currente_node.left)
#         else:
#             print('L:-1', end=',')
#         if currente_node.right != None:
#             print('R:', end='')
#             print(currente_node.right.data, end=",")
#             q.put(currente_node.right)
#         else:
#             print('R:-1', end=',')
#         print()

def printTreeDetail(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L",root.left.data, end=",")
    if root.right != None:
        print("R", root.right.data)
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)

# def takeInput():
#     q = queue.Queue()
#     print("Enter root")
#     rootData = int(input())
#     if rootData == -1:
#         return None
#     root = BinaryTreeNode(rootData)
#     q.put(root)
#     while (not(q.empty())):
#         current_node = q.get()
#         print("Enter the left data of root", current_node.data)
#         leftChildData = int(input())
#         if leftChildData != -1:
#             leftChild = BinaryTreeNode(leftChildData)
#             current_node.left = leftChild
#             q.put(leftChild)
#         print("Enter the right child of data", current_node.data)
#         rightChildData = int(input())
#         if rightChildData != -1:
#             rigntChild = BinaryTreeNode(rightChildData)
#             current_node.right = rigntChild
#             q.put(rigntChild)
#     return root


# def printTreeDetail(root, level=0, prefix='Root: '):
#     if root is None:
#         return
#     print(' ' * (level * 2) + prefix + str(root.data))
#     printTreeDetail(root.left, level + 1, 'L -- ')
#     printTreeDetail(root.right, level + 1, 'R -- ')
def printTreeInorderPreorder(pre, inorder):
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    inorderIndex = -1
    for i in range(0,len(inorder)):
        if inorder[i]==rootData:
            inorderIndex = i
            break
    if inorderIndex == -1:
        return None
    leftInorder = inorder[0:inorderIndex]
    rightInorder = inorder[inorderIndex+1:]

    lenLeftSubTree = len(leftInorder)
    leftPreorder = pre[1:lenLeftSubTree+1]
    rightPreorder = pre[lenLeftSubTree+1:]
    leftChild = printTreeInorderPreorder(leftInorder, leftPreorder)
    rightChild = printTreeInorderPreorder(rightInorder, rightPreorder)

    root.left = leftChild
    root.right = rightChild
    return root

pre = [int(x) for x in input().split()]
inorder = [int(y) for y in input().split()]
root = printTreeInorderPreorder(pre, inorder)

print("Binary Tree Details:")
printTreeDetail(root)
