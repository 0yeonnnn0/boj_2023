from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 초기 설정
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0

shark_size = 2
shark_eat = 0
shark_time = 0

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색 함수
def bfs(x, y, size):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(x, y, 0)])  # (x, y, 이동 거리)
    visited[x][y] = True
    possible_fish = []
    min_distance = float('inf')

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] <= size:  # 상어가 지나갈 수 있는 경우
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

                    if 0 < space[nx][ny] < size:  # 먹을 수 있는 물고기 발견
                        if dist + 1 < min_distance:
                            possible_fish = [(nx, ny, dist + 1)]
                            min_distance = dist + 1
                        elif dist + 1 == min_distance:
                            possible_fish.append((nx, ny, dist + 1))

    if possible_fish:
        possible_fish.sort()
        return possible_fish[0]
    else:
        return None

# 아기 상어의 행동 반복
while True:
    result = bfs(shark_x, shark_y, shark_size)
    if result is None:
        break

    nx, ny, distance = result
    shark_time += distance
    shark_x, shark_y = nx, ny
    space[nx][ny] = 0
    shark_eat += 1

    if shark_eat == shark_size:
        shark_size += 1
        shark_eat = 0

print(shark_time)