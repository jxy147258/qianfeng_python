import collections

queue = collections.deque()
print(queue)

queue.append("A")
print(queue)
queue.append("b")
print(queue)
queue.append("c")
print(queue)

res1 = queue.popleft()
print("res1 = ",res1)
print(queue)