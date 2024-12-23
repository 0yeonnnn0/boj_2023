import sys
import heapq

input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])
    lectures = []

    for i in range(1, N + 1):
        _, start, end = map(int, data[i].split())
        lectures.append((start, end))

    lectures.sort()
    min_heap = []

    for start, end in lectures:
        if min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)  # 강의실 재사용
        heapq.heappush(min_heap, end)  # 새로운 강의실 추가

    print(len(min_heap))  # 필요한 강의실 수 출력

if __name__ == '__main__':
    main()