def bubble_sort(lst, K):
    n = len(lst)
    swap_count = 0

    for last in range(n, 1, -1):
        for i in range(last - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap_count += 1

                if swap_count == K:
                    return lst

    return None


n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = bubble_sort(arr, k)

if result is not None:
    print(" ".join(map(str, result)))
else:
    print(-1)
