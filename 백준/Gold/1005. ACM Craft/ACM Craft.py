import sys
from collections import deque
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수 입력
for _ in range(T):
    N, K = map(int, input().split())  # 건물 수 N과 규칙 수 K 입력
    time = [0] + list(map(int, input().split()))  # 각 건물의 건설 시간 입력
    indegree = [0] * (N + 1)  # 진입 차수 배열 초기화
    graph = [[] for _ in range(N + 1)]  # 인접 리스트 초기화
    for _ in range(K):
        X, Y = map(int, input().split())  # 건설 순서 X -> Y 입력
        graph[X].append(Y)
        indegree[Y] += 1  # 진입 차수 증가
    W = int(input())  # 목표 건물 번호 입력
    dp = [0] * (N + 1)  # 각 건물까지의 최소 시간 저장 배열
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)  # 진입 차수가 0인 노드 큐에 삽입
            dp[i] = time[i]  # 건설 시간 초기화
    while q:
        current = q.popleft()  # 큐에서 노드 추출
        for next_node in graph[current]:
            indegree[next_node] -= 1  # 다음 노드 진입 차수 감소
            dp[next_node] = max(dp[next_node], dp[current] + time[next_node])  # 최대 시간 갱신
            if indegree[next_node] == 0:
                q.append(next_node)  # 진입 차수가 0이면 큐에 삽입
    print(dp[W])  # 목표 건물의 최소 시간 출력