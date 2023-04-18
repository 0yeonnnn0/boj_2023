K = int(input())
gaesu = 0
List = []

for i in range(0, K):
    a = int(input())

    if (a == 0):
        del List[gaesu-1]
        gaesu -= 1
    else:
        List.append(a)
        gaesu += 1

print(sum(List))