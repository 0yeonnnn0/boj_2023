from collections import deque

N = int(input())
time = [0] * N
indegree = [0] * N
graph = [[] for _ in range(N)]

for i in range(N):
    data = list(map(int, input().split()))
    time[i] = data[0]
    count = data[1]
    for j in range(count):
        graph[data[j + 2] - 1].append(i)
        indegree[i] += 1

queue = deque()
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)

completion_time = [0] * N
while queue:
    current = queue.popleft()
    completion_time[current] += time[current]
    for next_task in graph[current]:
        indegree[next_task] -= 1
        if indegree[next_task] == 0:
            queue.append(next_task)
        completion_time[next_task] = max(completion_time[next_task], completion_time[current])

print(max(completion_time))