class PriorityQueueNode:
    def __init__(self,value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)
    def isEmpty(self):
        return self.getSize()==0
    def getMax(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value
    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex>0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority>self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[childIndex]
                childIndex  = parentIndex
            else:
                break
    def insertMax(self, value, priority):
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        while parentIndex<self.getSize():
            leftChildIndex = 2*parentIndex+1
            rightChildIndex = 2*parentIndex+2
            maxIndex = parentIndex
            if leftChildIndex<self.getSize() and self.pq[leftChildIndex].priority>self.pq[maxIndex].priority:
                maxIndex = leftChildIndex
            if rightChildIndex<self.getSize() and self.pq[rightChildIndex].priority>self.pq[maxIndex].priority:
                maxIndex = rightChildIndex
            if maxIndex == parentIndex:
                break
            self.pq[parentIndex], self.pq[maxIndex] = self.pq[parentIndex],self.pq[maxIndex]
            parentIndex = maxIndex
    
    def removeMax(self):
        if self.isEmpty():
            return None
        ans = self.pq[0].value
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__percolateDown()
        return ans
        

    

pq = PriorityQueue()
pq.insertMax("A",89)
pq.insertMax("B",7)
pq.insertMax("C",3)

for i in range(3):
    print(pq.removeMax())

# class PriorityQueueNode:
#     def __init__(self, value, priority):
#         self.value = value
#         self.priority = priority

# class PriorityQueue:
#     def __init__(self):
#         self.pq = []

#     def getSize(self):
#         return len(self.pq)
    
#     def isEmpty(self):
#         return self.getSize() == 0
    
#     def getMax(self):
#         if self.isEmpty():
#             return None
#         return self.pq[0].value
    
#     def __percolateUp(self):
#         childIndex = self.getSize() - 1
#         while childIndex > 0:
#             parentIndex = (childIndex - 1) // 2
#             if self.pq[childIndex].priority > self.pq[parentIndex].priority:
#                 self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
#                 childIndex = parentIndex
#             else:
#                 break
    
#     def insertMax(self, value, priority):
#         pqNode = PriorityQueueNode(value, priority)
#         self.pq.append(pqNode)
#         self.__percolateUp()

#     def __percolateDown(self):
#         parentIndex = 0
#         while parentIndex < self.getSize():
#             leftChildIndex = 2 * parentIndex + 1
#             rightChildIndex = 2 * parentIndex + 2
#             maxIndex = parentIndex
            
#             if leftChildIndex < self.getSize() and self.pq[leftChildIndex].priority > self.pq[maxIndex].priority:
#                 maxIndex = leftChildIndex
#             if rightChildIndex < self.getSize() and self.pq[rightChildIndex].priority > self.pq[maxIndex].priority:
#                 maxIndex = rightChildIndex
            
#             if maxIndex == parentIndex:
#                 break
            
#             self.pq[parentIndex], self.pq[maxIndex] = self.pq[maxIndex], self.pq[parentIndex]
#             parentIndex = maxIndex
    
#     def removeMax(self):
#         if self.isEmpty():
#             return None
#         ans = self.pq[0].value
#         self.pq[0] = self.pq[self.getSize() - 1]
#         self.pq.pop()
#         self.__percolateDown()
#         return ans

# pq = PriorityQueue()
# pq.insertMax("A", 89)
# pq.insertMax("B", 7)
# pq.insertMax("C", 3)

# for i in range(3):
#     print(pq.removeMax())
