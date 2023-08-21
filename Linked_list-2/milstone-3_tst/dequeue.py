# from math import *
# from collections import *
# from sys import *
# from os import *

# # ## Read input as specified in the question.
# # ## Print output as specified in the question.

# class Dequeue:
#     def __init__(self):
#         self.size = 10
#         self.queue = [None] * self.size
#         self.front = -1
#         self.rear = -1

#     def insertFront(self, element):
#         if (self.front == 0 and self.rear == self.size - 1) or self.front == self.rear + 1:
#             print(-1)
#             return
#         elif self.front == -1:
#             self.front = 0
#             self.rear = 0
#         elif self.front == 0:
#             self.front = self.size - 1
#         else:
#             self.front = self.front - 1

#         self.queue[self.front] = element

#     def insertRear(self, element):
#         if (self.front == 0 and self.rear == self.size - 1) or self.front == self.rear + 1:
#             print(-1)
#             return
#         elif self.front == -1:
#             self.front = 0
#             self.rear = 0
#         elif self.rear == self.size - 1:
#             self.rear = 0
#         else:
#             self.rear = self.rear + 1

#         self.queue[self.rear] = element

#     def deleteFront(self):
#         if self.front == -1:
#             print(-1)
#             return

#         if self.front == self.rear:
#             self.front = -1
#             self.rear = -1
#         elif self.front == self.size - 1:
#             self.front = 0
#         else:
#             self.front = self.front + 1

#     def deleteRear(self):
#         if self.rear == -1:
#             print(-1)
#             return

#         if self.front == self.rear:
#             self.front = -1
#             self.rear = -1
#         elif self.rear == 0:
#             self.rear = self.size - 1
#         else:
#             self.rear = self.rear - 1

#     def getFront(self):
#         if self.front == -1:
#             return -1
#         return self.queue[self.front]

#     def getRear(self):
#         if self.rear == -1:
#             return -1
#         return self.queue[self.rear]


# # Main Function
# deque = Dequeue()
# input_list= input().split()

# for i in range(len(input_list)):
#     choice = input_list[i]
#     if choice == "1":
#         element = int(input_list[i+1])
#         deque.insertFront(element)
#     elif choice == "2":
#         element = int(input_list[i+1])
#         deque.insertRear(element)
#     elif choice == "3":
#         deque.deleteFront()
#     elif choice == "4":
#         deque.deleteRear()
#     elif choice == "5":
#         front = deque.getFront()
#         print(front)
#     elif choice == "6":
#         rear = deque.getRear()
#         print(rear)
#     elif choice == "-1":
#         break

# second approach

class Queueusingarray:
    def __init__(self):
        self.__arr = []
        self.__count = 0
    def insertRear(self,data):
        if self.__count == 10:
            return -1
        self.__arr.append(data)
        self.__count +=1
        return self.__arr
    def insertFront(self, data):
        if self.__count == 10:
            return -1
        self.__arr = [data]+self.__arr
        self.__count +=1
        return self.__arr
    def deleteRear(self):
        if self.__count == 0:
            print(-1)
            return
        self.__arr.pop(-1)
        self.__count -=1
        return self.__arr
    def deleteFront(self):
        if self.__count == 0:
            print(-1)
            return
        self.__arr.pop(0)
        self.__count -=1
        return self.__arr
    def getRear(self):
        if self.__count==0:
            return -1
        return self.__arr[-1]
    def getFront(self):
        if self.__count == 0:
            return -1
        return self.__arr[0]
    
t = [int(x) for x in input().split(" ")]
i = 0
A = Queueusingarray()

while t[i] != -1:
    n = t[i]
    i += 1
    if n == 1:
        k = A.insertFront(t[i])
        if k == -1:
            print(k)
        i += 1
    elif n == 2:
        k = A.insertRear(t[i])
        if k == -1:
            print(k)
        i+=1
    elif n == 3:
        A.deleteFront()
    elif n ==4:
        A.deleteRear()
    elif n == 5:
        print(A.getFront())
    elif n == 6:
        print(A.getRear())