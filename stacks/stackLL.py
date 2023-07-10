# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class stack:
#     def __init__(self):
#         self.__head = None
#         self.__count = 0

#     def push(self,element):
#         newNode = Node(element)
#         newNode.next = self.__head
#         self.__head = newNode
#         self.__count = self.__count +1
    
#     def pop(self):
#         if self.isEmpty():
#             print("Hey! Stack is Empty")
#             return
#         data = self.__head.data
#         self.__head = self.__head.next
#         self.__count = self.__count -1
#         return data
#     def top(self):
#         if self.isEmpty():
#             print("Hey! Stack is Empty")
#             return
#         data = self.__head.data
#         return data
#     def size(self):
#         return self.__count
#     def isEmpty(self):
#         return self.size()==0

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.count = self.count+1

    def pop(self):
        if self.isEmpty():
            return
        data = self.head.data
        self.head = self.head.next
        self.count = self.count -1
        return data
    def top(self):
        if self.isEmpty():
            return
        data = self.head.data
        return data
    def size(self):
        return self.count
    def isEmpty(self):
        return self.size()==0
