N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A를 오름차순 정렬
A.sort()
# B를 내림차순 정렬
B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)