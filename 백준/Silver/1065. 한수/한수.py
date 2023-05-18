n = int(input())

hansu_gaesu = 0

for i in range(1,n+1):
    numlist = list(map(int, str(i)))

    if len(numlist) <= 2:
        hansu_gaesu += 1
    elif (numlist[0] + numlist[2])/2 == numlist[1]:
        hansu_gaesu += 1
    else:
        pass

print(hansu_gaesu)