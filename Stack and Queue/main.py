import queue, stack

q = stack.Stack()
q.push(5)
q.push(10)
q.push(15)
q.push(20)
print(q.size())
print(q.peek())
print(q.pop())
print(q.pop())
print(q.is_empty())