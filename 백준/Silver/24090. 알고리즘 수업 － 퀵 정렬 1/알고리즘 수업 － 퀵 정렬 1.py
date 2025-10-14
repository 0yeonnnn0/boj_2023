import sys

sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline


def quick_sort(A, p, r):
    if p >= r:
        return
    q = partition(A, p, r)
    quick_sort(A, p, q - 1)
    quick_sort(A, q + 1, r)


def partition(A, p, r):
    global swap_count, K

    x = A[r]  # 기준원소
    i = p - 1  # i = x보다 작거나 같은 원소들의 끝지점

    # j = 아직 정해지지 않은 원소들의 시작 지점
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            # A[i], A[j] 교환
            A[i], A[j] = A[j], A[i]
            swap_count += 1
            if swap_count == K:
                print(A[i], A[j])
                sys.exit()

    # i + 1과 r이 서로 다르면 A[i + 1], A[r]을 교환
    if i + 1 != r:
        A[i + 1], A[r] = A[r], A[i + 1]
        swap_count += 1
        if swap_count == K:
            print(A[i + 1], A[r])
            sys.exit()

    return i + 1


# 입력 받기
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 전역 변수
swap_count = 0

# 퀵 정렬 실행
quick_sort(A, 0, N - 1)

# K번째 교환을 찾지 못한 경우
print(-1)
