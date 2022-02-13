# First in, First out, FIFO

class Queue:
    def __init__(self):
        self.size = 0
        self.li = []
    
    def put(self, data):
        self.size += 1
        self.li.append(data)
    
    def get(self):
        self.size -= 1
        return self.li.pop(0)
    
    def getSize(self):
        return self.size

q = Queue()

q.put('hello')
q.put('there')
q.put(34331244)

size = q.getSize()
for i in range(size):
    print(q.get())



    # Deque (both sides)
    # Heap (gets the most important number)
    # Priority Queue (^)

    # Maps
    # Dictionaries
    # Graphs