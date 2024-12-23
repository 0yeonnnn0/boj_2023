N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # A를 오름차순 정렬
B.sort(reverse=True)  # B를 내림차순 정렬

S = 0
for i in range(N):
    S += A[i] * B[i]  # A와 B의 각 요소의 곱을 S에 더함

print(S)  # 최소 S 값 출력