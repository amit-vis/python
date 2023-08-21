class BinaryNodeTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def diametere(root):
    if root == None:
        return 0, 0
    lh,ld = diametere(root.left)
    rh,rd = diametere(root.right)
    h = 1+ max(lh,rh)
    diametere_root = rh+lh
    diametere_of = max(diametere_root, ld, rd)
    return h, diametere_of

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
    root = BinaryNodeTree(rootData)
    root.left = takeInput()
    root.right = takeInput()
    return root

root = takeInput()
printData(root)
print(diametere(root))