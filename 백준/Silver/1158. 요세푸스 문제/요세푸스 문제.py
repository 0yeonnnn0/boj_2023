from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
result = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())  # K-1번째 사람을 뒤로 보냄
    result.append(queue.popleft())  # K번째 사람을 제거하고 결과에 추가

print('<' + ', '.join(map(str, result)) + '>')