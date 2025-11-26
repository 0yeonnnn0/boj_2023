import sys
input = sys.stdin.readline

NEG_INF = -10**18  # 매우 작은 값으로 초기화


def bellman_ford_max_profit(n, start, end, edges, earn):
    # 각 도시에 도달했을 때 벌 수 있는 최대 돈
    dist = [NEG_INF] * n
    dist[start] = earn[start]

    # n-1번 완화
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] == NEG_INF:
                continue
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # 도착 자체가 불가능한 경우
    if dist[end] == NEG_INF:
        return "gg"

    # 양의 사이클(= 무한히 돈 벌 수 있는 경로) 존재 여부 확인
    # dist 값이 더 커질 수 있는 정점이 있고,
    # 그 정점에서 end로 도달 가능한 경로가 있다면 Gee
    reachable = [False] * n
    for u, v, w in edges:
        if dist[u] == NEG_INF:
            continue
        if dist[u] + w > dist[v]:
            reachable[v] = True

    # 긍정 사이클에서 출발해서 end까지 도달 가능한지 BFS로 검사
    from collections import deque
    q = deque()

    for i in range(n):
        if reachable[i]:
            q.append(i)

    reachable_from_cycle = [False] * n
    while q:
        cur = q.popleft()
        if reachable_from_cycle[cur]:
            continue
        reachable_from_cycle[cur] = True
        for u, v, w in edges:
            if u == cur and not reachable_from_cycle[v]:
                q.append(v)

    if reachable_from_cycle[end]:
        return "Gee"

    # 사이클 영향 없으면 최대 수익 출력
    return dist[end]


def main():
    n, start, end, m = map(int, input().split())
    edges = []

    # 간선 입력: (출발, 도착, 교통비(음수))
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append([a, b, -c])  # 교통비는 음수 처리

    earn = list(map(int, input().split()))

    # 간선 가중치에 도착 도시에서 벌 수 있는 돈 더하기
    for i in range(m):
        u, v, w = edges[i]
        edges[i][2] = w + earn[v]

    result = bellman_ford_max_profit(n, start, end, edges, earn)
    print(result)


if __name__ == "__main__":
    main()
