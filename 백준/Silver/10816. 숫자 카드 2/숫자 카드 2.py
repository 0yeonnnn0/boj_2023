import sys
input = sys.stdin.readline          #시간초과 꿀팁, strip() 뒤에 붙이기

n = int(input())                    #n에 숫자 카드의 개수를 입력받음
cardlist = list(map(int, input().split())) #다음줄에 card의 리스트를 만듬

carddic = {}                        #cardlist 딕셔너리로 만들기
for i in cardlist:
    if i in carddic:
        carddic[i] += 1
    else:
        carddic[i] = 1

m = int(input())                    #m에 몇번 구할건지 받기
hascard = list(map(int, input().split()))   #다음줄에 몇번이 궁금한지 받기
result = []
for i in hascard:
    if i in carddic:
        result.append(carddic.get(i))
    else:
        result.append(0)
print(*result)