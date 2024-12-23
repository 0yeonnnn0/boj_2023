N, P, Q = map(int, input().split())
memo = {}

def A(i):
    if i == 0:
        return 1
    if i in memo:
        return memo[i]
    memo[i] = A(i // P) + A(i // Q)
    return memo[i]

print(A(N))