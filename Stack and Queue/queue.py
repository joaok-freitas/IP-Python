class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() > 0:
            return self.items[0]
        else:
            return None

    def isempty(self):
        return self.size() == 0

    def empty(self):
        self.items = []


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
y = q.dequeue()
print(y)
z = q.dequeue()
print(z)
print(q.dequeue())
print(q.dequeue())