N = int(input())
max_gold_number = 0

for number in range(4, N + 1):
    num_str = str(number)
    if all(digit in '47' for digit in num_str):
        if number > max_gold_number:
            max_gold_number = number

print(max_gold_number)