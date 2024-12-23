def matrix_chain_order(dimensions):
    N = len(dimensions) - 1
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for chain_length in range(2, N + 1):
        for i in range(1, N - chain_length + 2):
            j = i + chain_length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][N]

N = int(input())
dimensions = []
for _ in range(N):
    r, c = map(int, input().split())
    if not dimensions:
        dimensions.append(r)
    dimensions.append(c)

print(matrix_chain_order(dimensions))