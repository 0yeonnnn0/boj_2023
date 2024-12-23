from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
result = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())  # K-1번 만큼 앞에서 꺼내 뒤로 삽입
    result.append(queue.popleft())  # K번째 사람 제거

print('<' + ', '.join(map(str, result)) + '>')