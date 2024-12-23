from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))
josephus_sequence = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())  # K-1번 앞의 사람을 뒤로 보냅니다
    josephus_sequence.append(queue.popleft())  # K번째 사람을 제거합니다

print('<' + ', '.join(map(str, josephus_sequence)) + '>')