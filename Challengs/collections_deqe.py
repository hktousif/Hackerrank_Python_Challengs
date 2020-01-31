from collections import deque

d = deque()
for _ in range(int(input())):
    li = input().split()
    if li[0] == 'append':
        d.append(int(li[1]))
    elif li[0] == 'pop':
        d.pop()
    elif li[0] == 'popleft':
        d.popleft()
    elif li[0] == 'appendleft':
        d.appendleft(int(li[1]))
for i in list(d):
    print(i, end=' ')