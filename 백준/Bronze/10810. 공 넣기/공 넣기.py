N, M = map(int, input().split())
basket = [0] * (N)

for x in range(0, M):
    i, j, k = map(int, input().split())
    for y in range(i-1, j):
        basket[y] = k

print(*basket)