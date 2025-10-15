import sys

# 재귀 깊이 제한 증가 (RecursionError 방지)
sys.setrecursionlimit(20000)

input = sys.stdin.readline

# 입력 받기
N, Q, K = map(int, input().split())
A = list(map(int, input().split()))

# 전역 변수
swap_count = 0
result = None


def swap(arr, i, j):
    global swap_count, result
    # 교환 수행
    arr[i], arr[j] = arr[j], arr[i]
    swap_count += 1

    # K번째 교환이면 결과 저장
    if swap_count == K:
        result = arr[:]


def partition(arr, p, r):
    if result is not None:  # 이미 결과를 찾았으면 조기 종료
        return r

    x = arr[r]  # 기준원소 (pivot)
    i = p - 1  # i는 x보다 작거나 같은 원소들의 끝 지점

    # j는 아직 정해지지 않은 원소들의 시작 지점
    for j in range(p, r):
        if result is not None:  # 결과를 찾으면 즉시 종료
            break
        if arr[j] <= x:
            i += 1
            swap(arr, i, j)  # A[++i] <-> A[j]

    # i + 1과 r이 서로 다르면 교환
    if result is None and i + 1 != r:
        swap(arr, i + 1, r)

    return i + 1


def select(arr, p, r, q):
    if result is not None:  # 이미 결과를 찾았으면 조기 종료
        return

    if p == r:
        return arr[p]

    t = partition(arr, p, r)  # 분할
    k = t - p + 1  # 기준원소가 전체에서 k번째 작은 원소임

    if q < k:
        return select(arr, p, t - 1, q)  # 왼쪽 그룹으로 범위를 좁힘
    elif q == k:
        return arr[t]  # 기준원소가 찾는 원소임
    else:
        return select(arr, t + 1, r, q - k)  # 오른쪽 그룹으로 범위를 좁힘


# 선택 알고리즘 실행
select(A, 0, N - 1, Q)

# 결과 출력
if result:
    print(" ".join(map(str, result)))
else:
    print(-1)
