from collections import deque

# BFS를 위한 방향 설정 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 입력 받기
N, M = map(int, input().split())
map_data = [list(map(int, input().strip())) for _ in range(N)]

# 방문 체크 배열 (3차원)
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

# BFS 큐 초기화
queue = deque([(0, 0, 0)])  # (x, y, 벽 부숨 여부)
visited[0][0][0] = True

distance = 1

while queue:
    for _ in range(len(queue)):
        x, y, wall_broken = queue.popleft()
        # 목표 지점에 도달한 경우
        if x == N - 1 and y == M - 1:
            print(distance)
            exit()
        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아니고 방문하지 않은 경우
                if map_data[nx][ny] == 0 and not visited[nx][ny][wall_broken]:
                    visited[nx][ny][wall_broken] = True
                    queue.append((nx, ny, wall_broken))
                # 벽이고 벽을 부수지 않은 경우
                elif map_data[nx][ny] == 1 and wall_broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1))
    distance += 1

# 경로를 찾지 못한 경우
print(-1)