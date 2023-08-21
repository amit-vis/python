class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def printTree(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print('L', root.left.data, end=',')
    if root.right != None:
        print('R', root.right.data)
    print()
    printTree(root.left)
    printTree(root.right)


def buildTreeUsing(post, inorder):
    if len(post) == 0:
        return None
    rootData = post[-1]
    root = BinaryTreeNode(rootData)
    inorderIndex = -1
    for i in range(0,len(inorder)):
        if inorder[i] == rootData:
            inorderIndex = i
            break

    if inorderIndex == -1:
        return None
    leftInorder = inorder[0:inorderIndex]
    rightInorder = inorder[inorderIndex+1:]

    leftSubTree = len(leftInorder)
    leftpostorder = post[0:leftSubTree]
    rightpostorder = post[leftSubTree:-1]

    root.left = buildTreeUsing(leftInorder, leftpostorder)
    root.right = buildTreeUsing(rightInorder, rightpostorder)
    return root

# a = [1, 2, 3, 4, 5]
# print(a[-1])

post = [int(x) for x in input().split()]
inorder = [int(y) for y in input().split()]
root = buildTreeUsing(post, inorder)

print("Binary Tree Details:")
printTree(root)