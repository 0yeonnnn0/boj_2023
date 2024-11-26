def find_smallest_constructor(N):
    # M의 가능한 시작 지점은 N - (9 * 자릿수의 개수)로 설정
    start = max(1, N - (len(str(N)) * 9))  
    
    for M in range(start, N):  # 가능한 M 범위 내에서 탐색
        # 분해합 계산
        decomposition_sum = M + sum(map(int, str(M)))
        
        if decomposition_sum == N:
            return M  # 가장 작은 생성자를 찾으면 반환
    
    return 0  # 생성자가 없는 경우

# 입력받기
N = int(input())
print(find_smallest_constructor(N))
