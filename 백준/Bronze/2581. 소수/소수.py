n = int(input())
m = int(input())

#n~m의 리스트 만들기
sosulist = []

#소수찾는법 : 2로나누고 3으로나누고 ...
for i in range(n, m+1):
    notsosu = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                notsosu += 1
                break
        if notsosu == 0:
            sosulist.append(i)

if len(sosulist) > 0:
    print(sum(sosulist))
    print(min(sosulist))
else:
    print(-1)