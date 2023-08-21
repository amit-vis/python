# class BinaryNodes:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None
#         self.numNodes = 0

#     def printTreeHelper(self, root):
#         if root == None:
#             return
#         print(root.data, end=":")
#         if root.left != None:
#             print('L:', root.left.data, end=',')
#         if root.right != None:
#             print('R:', root.right.data)
#         print()
#         self.printTreeHelper(root.left)
#         self.printTreeHelper(root.right)

#     def printTree(self):
#         self.printTreeHelper(self.root)

#     def isPresentHelper(self, root, data):
#         if root == None:
#             return False
#         if root.data == data:
#             return True
#         if root.data > data:
#             return self.isPresentHelper(root.left, data)
#         else:
#             return self.isPresentHelper(root.right, data)

#     def isPresent(self, data):
#         return self.isPresentHelper(self.root, data)
    
#     def insertHelper(self,root,data):
#         if root == None:
#             Node = BinaryNodes(data)
#             return Node
#         if root.data>data:
#             root.left = self.insertHelper(root.left)
#             return root
#         else:
#             root.right = self.insertHelper(root.right,data)
#             return root
    
#     def insert(self, data):
#         self.numNodes +=1
#         self.root = self.insertHelper(self.root, data)

#     def min(self, root):
#         if root == None:
#             return 1000000
#         if root.left == None:
#             return root.data
#         return self.min(root.left)

#     def deleteDataHelper(self,root,data):
#         if root == None:
#             return False, None
#         if root.data > data:
#             delete, newNodeLeft = self.deleteDataHelper(root.left, data)
#             root.left = newNodeLeft
#             return delete, root
#         if root.data < data:
#             delete, newNodeRight = self.deleteDataHelper(root.right,data)
#             root.right = newNodeRight
#             return delete, root
#         if root.left == None and root.right == None:
#             return True, None
#         if root.left == None:
#             return True, root.right
#         if root.right == None:
#             return True, root.left
        
#         replacement = self.min(root.data)
#         root.data = replacement
#         delete, newNodeRight = self.deleteDataHelper(root.right, replacement)
#         root.right = newNodeRight
#         return True, newNodeRight

    
#     def deleteData(self, data):
#         deleted, newRoot = self.deleteDataHelper(self.root, data)
#         if deleted:
#             self.numNodes -= 1
#         self.root = newRoot
#         return deleted
#     def count(self):
#         return self.numNodes
    

# b = BST()
# b.insert(5)
# b.insert(10)
# b.insert(12)
# b.printTree()
# print(b.count())

class BinaryNodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def isPresentHelper(self,root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        if root.data> data:
            return self.isPresentHelper(root.left)
        else:
            return self.isPresentHelper(root.right)

    def isPresent(self, data):
        return self.isPresentHelper(self.root, data)
    
    def insertHelper(self, root, data):
        if root == None:
            newNode = BinaryNodeTree(data)
            return newNode
        if root.data> data:
            root.left = self.insertHelper(root.left)
            return root
        else:
            root.right = self.insertHelper(root.right,data)
            return root

    def insert(self,data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)

    def deleteDataHelper(self,root, data):
        if root == None:
            return False, None
        if root.data > data:
            deleted, newLeftNode = self.deleteDataHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        if root.data < data:
            deleted, newRightNode = self.deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        if root.left == None and root.right == None:
            return True, None
        if root.left == None:
            return True, root.right
        if root.right == None:
            return True, root.left
        
        replacement = self.min(root.data)
        root.data = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True, newRightNode


    def deleteData(self, data):
        deleted, newRoot = self.deleteDataHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted
    def count(self):
        return self.numNodes

    def count(self):
        return self.numNodes

    def printTreeHelper(self,root):
        if root == None:
            return
        print(root.data, end=':')
        if root.left != None:
            print("L:", root.left.data, end=',')
        if root.right != None:
            print('R:', root.right.data)
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

b = BST()
b.insert(5)
b.insert(10)
b.insert(12)
b.printTree()
print(b.count())
