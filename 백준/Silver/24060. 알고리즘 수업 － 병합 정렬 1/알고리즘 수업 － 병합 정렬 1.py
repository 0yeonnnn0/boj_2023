count = 0
result = -1
K = 0


def merge_sort(A, p, r):
    # 배열 A[p..r]을 오름차순으로 정렬
    if p < r:
        q = (p + r) // 2  # 중간 지점
        merge_sort(A, p, q)  # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)  # 병합


def merge(A, p, q, r):
    # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순으로 정렬
    global count, result, K

    i = p  # 왼쪽 부분 배열의 시작 인덱스
    j = q + 1  # 오른쪽 부분 배열의 시작 인덱스
    tmp = []  # 임시 배열

    # 두 부분 배열을 비교하며 병합
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    # 왼쪽 배열 부분이 남은 경우
    while i <= q:
        tmp.append(A[i])
        i += 1

    # 오른쪽 배열 부분이 남은 경우
    while j <= r:
        tmp.append(A[j])
        j += 1

    # 결과를 A[p..r]에 저장 (이 부분에서 저장 횟수 카운트)
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:
            result = A[i]
        i += 1
        t += 1


# N = 배열 A의 크기
# K = 저장 횟수
# A = 정렬할 숫자 배열
N, K = map(int, input().split())
A = list(map(int, input().split()))

merge_sort(A, 0, N - 1)
print(result)
