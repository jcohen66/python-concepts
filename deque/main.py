from collections import deque

people = ["Mario", "Luigi", "Toad"]
queue = deque(people)

queue.append("Bowser")
print(queue)

queue.popleft()
print(queue)

queue.appendleft("Daisy")
print(queue)

queue.rotate(-1)
print(queue)

queue.rotate(-2)
print(queue)

queue.rotate()
print(queue)

queue.extendleft(["Shy Guy", "Yoshi"])
print(queue)

queue.reverse()
print(queue)
