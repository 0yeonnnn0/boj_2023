T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        start_inside = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        end_inside = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2
        if start_inside != end_inside:
            count += 1
    print(count)