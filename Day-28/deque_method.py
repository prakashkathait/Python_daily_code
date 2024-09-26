from collections import deque

N = int(input())
d = deque()  # initialize deque
for i in range(N):
    inputs = input().split()
    method = inputs[0]
    if len(inputs) > 1:
        value = int(inputs[1])

    if method == 'append':
        d.append(value)
    elif method == 'appendleft':
        d.appendleft(value)
    elif method == 'clear':
        d.clear()
    elif method == 'extend':
        d.extend(map(int, inputs[1:]))  # extend expects an iterable, so you need to handle it differently
    elif method == 'extendleft':
        d.extendleft(map(int, inputs[1:]))
    elif method == 'count':
        d.count(value)
    elif method == 'pop':
        d.pop()
    elif method == 'popleft':
        d.popleft()
    elif method == 'remove':
        d.remove(value)
    elif method == 'reverse':
        d.reverse()
    elif method == 'rotate':
        d.rotate(value)

print(" ".join(map(str, d)))
