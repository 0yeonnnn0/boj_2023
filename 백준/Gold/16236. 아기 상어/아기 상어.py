from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 초기 설정
shark_size = 2
fish_eaten = 0
total_time = 0

# 아기 상어의 초기 위치 찾기
def find_shark():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                grid[i][j] = 0
                return i, j

# BFS를 사용하여 물고기를 찾는 함수
def bfs(shark_pos):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([shark_pos])
    visited = [[False] * N for _ in range(N)]
    visited[shark_pos[0]][shark_pos[1]] = True
    min_distance = float('inf')
    target_fish = None
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
                            if distance + 1 < min_distance:
                                min_distance = distance + 1
                                target_fish = (nx, ny)
                            elif distance + 1 == min_distance:
                                if target_fish:
                                    if (nx < target_fish[0]) or (nx == target_fish[0] and ny < target_fish[1]):
                                        target_fish = (nx, ny)
        distance += 1
        if target_fish:
            break
    return target_fish, min_distance

shark_pos = find_shark()

# 반복적으로 물고기를 먹기
while True:
    target_fish, min_distance = bfs(shark_pos)
    if not target_fish:
        break

    # 물고기를 먹고 위치 및 시간 업데이트
    shark_pos = target_fish
    grid[shark_pos[0]][shark_pos[1]] = 0
    total_time += min_distance
    fish_eaten += 1

    # 상어 크기 증가
    if fish_eaten == shark_size:
        shark_size += 1
        fish_eaten = 0

print(total_time)