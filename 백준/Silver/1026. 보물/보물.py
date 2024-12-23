N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # A를 오름차순으로 정렬
B.sort(reverse=True)  # B를 내림차순으로 정렬

S = 0
for i in range(N):
    S += A[i] * B[i]  # 각 인덱스의 곱을 S에 더함

print(S)  # S의 최솟값 출력