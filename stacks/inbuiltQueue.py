import queue

# q = queue.Queue()
# q.put(1)
# q.put(3)
# q.put(5)
# q.put(6)

# while not q.empty():
#     print(q.get())

q = queue.LifoQueue()
q.put(3)
q.put(87)
q.put(8)

while not q.empty():
    print(q.get())