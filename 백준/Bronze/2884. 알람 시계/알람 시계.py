H, M = map(int, input().split())
M -= 45  # 45분 빼기
if M < 0:  # 분이 음수가 될 경우
    M += 60  # 분을 60분에서 부족한 만큼 더함
    H -= 1  # 시간을 한 시간 줄임
    if H < 0:  # 시간이 음수가 될 경우
        H = 23  # 시간을 23시로 설정
print(H, M)  # 결과 출력