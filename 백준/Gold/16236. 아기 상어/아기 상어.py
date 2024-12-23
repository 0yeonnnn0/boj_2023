from collections import deque

# BFS를 사용하여 아기 상어가 먹을 수 있는 가장 가까운 물고기를 찾습니다.
def bfs(shark_position, shark_size, grid, N):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([shark_position])
    visited = [[False] * N for _ in range(N)]
    visited[shark_position[0]][shark_position[1]] = True
    fish_list = []
    distance = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if grid[nx][ny] <= shark_size:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        if 0 < grid[nx][ny] < shark_size:
                            fish_list.append((distance + 1, nx, ny))
        distance += 1
        if fish_list:
            break

    fish_list.sort()
    return fish_list[0] if fish_list else None

# 메인 함수
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
shark_position = (0, 0)

# 아기 상어의 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            shark_position = (i, j)
            grid[i][j] = 0
            break

time = 0
eaten_fish_count = 0

while True:
    result = bfs(shark_position, shark_size, grid, N)
    if not result:
        break

    distance, nx, ny = result
    time += distance
    shark_position = (nx, ny)
    grid[nx][ny] = 0
    eaten_fish_count += 1

    if eaten_fish_count == shark_size:
        shark_size += 1
        eaten_fish_count = 0

print(time)