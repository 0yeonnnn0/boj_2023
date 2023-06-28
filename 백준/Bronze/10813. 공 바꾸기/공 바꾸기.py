N, M = map(int, input().split())
basket = list(range(1, N+1))

for x in range(0, M):
    i, j = map(int, input().split())
    x = basket[i-1]
    y = basket[j-1]
    basket[i-1] = y
    basket[j-1] = x

print(*basket)