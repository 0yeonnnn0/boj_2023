N = int(input())
largest_gold_number = 0

for i in range(N, 3, -1):
    is_gold_number = True
    for digit in str(i):
        if digit != '4' and digit != '7':
            is_gold_number = False
            break
    if is_gold_number:
        largest_gold_number = i
        break

print(largest_gold_number)