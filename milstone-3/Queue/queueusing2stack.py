class Queueusingtwostack:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, item):
        while (len(self.__s1) != 0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(item)
        while (len(self.__s2) != 0):
            self.__s1.append(self.__s2.pop())

    def dequeue(self):
        if (len(self.__s1) == 0):
            return -1
        return self.__s1.pop()
    def size(self):
        return len(self.__s1)

    def isEmpty(self):
        return self.size()==0

    def front(self):
        if self.__s1 == 0:
            return -1
        return self.__s1[-1]
    

q = Queueusingtwostack()
q.enqueue(5)
q.enqueue(3)
q.enqueue(6)
q.enqueue(7)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()