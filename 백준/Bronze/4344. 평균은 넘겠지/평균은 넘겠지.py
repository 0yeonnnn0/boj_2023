C = int(input())

for i in range(C):
    stu_list = list(map(float, input().split()))
    N = stu_list[0]
    stu_many = 0

    avr = round((sum(stu_list[1:]))/N, 4)

    for i in stu_list[1:]:
        if i > avr:
            stu_many += 1

    print("{:.3f}%".format((stu_many/N)*100))