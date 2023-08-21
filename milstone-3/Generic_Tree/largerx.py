import queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def largerNum(root, x):
    ans = None
    if root == None:
        return ans
    if root.data> x:
        ans = root

    for child in root.children:
        temp = largerNum(child,x)
        if temp:
            if (not ans) or (ans.data>temp.data):
                ans = temp
    return ans


def printTree(root):
    if root == None:
        return
    print(root.data, ":", end='')
    for child in root.children:
        print(child.data, ',', end='')
    print()
    for child in root.children:
        printTree(child)

def takeInput():
    q= queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        current_node = q.get()
        print("Enter the number of children", current_node.data)
        numchildren = int(input())
        for i in range(numchildren):
            print("Enter the next child")
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root

root = takeInput()
printTree(root)
x = int(input())
print(largerNum(root, x))
