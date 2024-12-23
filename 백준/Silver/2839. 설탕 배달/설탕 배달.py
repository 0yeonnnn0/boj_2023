def sugar_delivery(n):
    # 5kg 봉지와 3kg 봉지의 개수를 최대로 조합해서 적은 봉지 수를 계산
    bags = 0

    while n >= 0:
        # 5의 배수로 만들 수 있는 경우
        if n % 5 == 0:
            bags += n // 5
            return bags
        # 5의 배수가 될 때까지 3을 빼면서 시도
        n -= 3
        bags += 1

    # 정확히 나누어 떨어지지 않는 경우
    return -1

# 입력 받기
n = int(input())
# 결과 출력
print(sugar_delivery(n))
