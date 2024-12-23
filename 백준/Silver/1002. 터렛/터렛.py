import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 두 원의 중심 거리 계산
    if d == 0 and r1 == r2:
        print(-1)  # 무한대의 교점
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)  # 내접 또는 외접
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)  # 두 개의 교점
    else:
        print(0)  # 교점 없음