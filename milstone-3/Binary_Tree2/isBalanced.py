class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
# def height(root):
#     if root == None:
#         return 0
#     leftCount = height(root.left)
#     rightCount = height(root.right)
#     if leftCount>rightCount:
#         return 1 + leftCount
#     else:
#         return 1 + rightCount
    
# def isBalanced(root):
#     if root == None:
#         return True
#     lh = height(root.left)
#     rh = height(root.right)
#     if (lh-rh)>1 or (rh-lh)>1:
#         return False
#     isBalancedLeft = isBalanced(root.left)
#     isBalancedRight = isBalanced(root.right)
#     if isBalancedLeft and isBalancedRight:
#         return True
#     else:
#         return False

# Improved code
def isBalancedImp(root):
    if root == None:
        return 0, True
    lh,isBalancedLeft = isBalancedImp(root.left)
    rh,isBalancedRight = isBalancedImp(root.right)
    h = 1+ max(lh,rh)
    if lh-rh>1 or rh-lh>1:
        return h, False
    if isBalancedLeft and isBalancedRight:
        return h, True
    else:
        return h , False

def printData(root):
    if root == None:
        return
    print(root.data, end=':')
    if root.left != None:
        print('L', root.left.data, end=',')
    if root.right != None:
        print('R', root.right.data)
    print()
    printData(root.left)
    printData(root.right)

def takeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
printData(root)
print(isBalancedImp(root))
