class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() > 0:
            return self.items.pop(-1)
        else:
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if self.size() > 0:
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return self.size() == 0

    def empty(self):
        self.items = []


q = Stack()
q.push(1)
q.push(2)
q.push(3)
q.push(5)
print(q.items)
q.pop()
print(q.items)
q.pop()
print(q.items)
q.pop()
print(q.items)
q.pop()
print(q.items)
q.pop()
print(q.items)