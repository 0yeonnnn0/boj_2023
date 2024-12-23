N = int(input())

for i in range(N, 3, -1):
    isGeumMinSu = True
    for digit in str(i):
        if digit != '4' and digit != '7':
            isGeumMinSu = False
            break
    if isGeumMinSu:
        print(i)
        break