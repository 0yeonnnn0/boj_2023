N, K = map(int, input().split())
people = list(range(1, N + 1))
result = []
index = 0

while people:
    index = (index + K - 1) % len(people)  # K번째 사람의 인덱스 계산
    result.append(people.pop(index))  # K번째 사람 제거 후 결과에 추가

print('<' + ', '.join(map(str, result)) + '>')  # 결과 출력