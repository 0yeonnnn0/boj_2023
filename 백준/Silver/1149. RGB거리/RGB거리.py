N = int(input())
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    r, g, b = map(int, input().split())
    if i == 0:
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b
    else:
        dp[i][0] = r + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = g + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = b + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))