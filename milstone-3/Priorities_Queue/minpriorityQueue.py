class PriorityQueueNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize()==0
    
    def getMin(self):
        if self.isEmpty() is True:
            return None
        return self.pq[0].value
    
    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex>0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex],self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    
    def insert(self, value, priority):
        pqNode = PriorityQueueNode(value, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        # parentIndex = 0
        # while parentIndex < self.getSize():
        #     lci = 2 * parentIndex + 1
        #     rci = 2 * parentIndex + 2
        #     minIndex = parentIndex
            
        #     if lci < self.getSize() and self.pq[lci].priority < self.pq[minIndex].priority:
        #         minIndex = lci
        #     if rci < self.getSize() and self.pq[rci].priority < self.pq[minIndex].priority:
        #         minIndex = rci
            
        #     if minIndex == parentIndex:
        #         break
            
        #     self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
        #     parentIndex = minIndex
        parentIndex = 0
        while parentIndex <self.getSize():
            lci = 2*parentIndex+1
            rci = 2*parentIndex+2
            minIndex = parentIndex
            if lci<self.getSize() and self.pq[lci].priority<self.pq[minIndex].priority:
                minIndex = lci
            if rci< self.getSize() and self.pq[rci].priority<self.pq[minIndex].priority:
                minIndex = rci
            if minIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
            parentIndex = minIndex
                

    def removeMin(self):
        ans = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ans

pq = PriorityQueue()
pq.insert('A',10)
pq.insert('B', 5)
pq.insert('c',15)
pq.insert('D',4)

for i in range(4):
    print(pq.remove())
