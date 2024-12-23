N, L, D = map(int, input().split())
current_time = 0

while True:
    # 노래와 조용한 구간을 고려한 전체 재생 시간
    total_play_time = (L + 5) * N - 5
    # 전화벨이 조용한 구간에 울리는지 확인
    if current_time > total_play_time or (current_time % (L + 5)) >= L:
        print(current_time)
        break
    # 전화벨 주기 만큼 증가
    current_time += D