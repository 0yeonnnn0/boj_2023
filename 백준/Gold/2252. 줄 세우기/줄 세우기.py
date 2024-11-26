from collections import deque

def topological_sort(N, edges):
    # 그래프와 진입 차수 초기화
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)

    # 그래프 및 진입 차수 구성
    for A, B in edges:
        graph[A].append(B)
        indegree[B] += 1

    # 진입 차수가 0인 노드를 큐에 삽입
    queue = deque([i for i in range(1, N + 1) if indegree[i] == 0])
    result = []

    # 위상 정렬 수행
    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result

# 입력 처리
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 위상 정렬 실행
result = topological_sort(N, edges)

# 결과 출력
print(*result)
