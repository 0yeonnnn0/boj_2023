N, kim, lim = map(int, input().split())
round = 0
while kim != lim:
    kim = (kim + 1) // 2  # 다음 라운드에서의 김지민 번호 계산
    lim = (lim + 1) // 2  # 다음 라운드에서의 임한수 번호 계산
    round += 1  # 라운드 증가
print(round)  # 대결 라운드 번호 출력