# from queue_using_array import queue

# q = queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(67)
# q.enqueue(7)

# while q.isEmpty() is False:
#     print(q.front())
#     q.dequeue()
# print(q.dequeue())

from QueueusingLL import QueueusingLL

q = QueueusingLL()
q.enqueue(3)
q.enqueue(7)
q.enqueue(8)
q.enqueue(36)

while q.isEmpty() is False:
    print(q.dequeue())