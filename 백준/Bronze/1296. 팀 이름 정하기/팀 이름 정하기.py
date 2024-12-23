yeondoo_name = input().strip()
N = int(input().strip())
best_team = ""
max_probability = -1

for _ in range(N):
    team_name = input().strip()
    count_L = count_O = count_V = count_E = 0
    for char in yeondoo_name + team_name:
        if char == 'L':
            count_L += 1
        elif char == 'O':
            count_O += 1
        elif char == 'V':
            count_V += 1
        elif char == 'E':
            count_E += 1
    probability = ((count_L + count_O) * (count_L + count_V) * (count_L + count_E) * (count_O + count_V) * (count_O + count_E) * (count_V + count_E)) % 100
    if probability > max_probability or (probability == max_probability and team_name < best_team):
        max_probability = probability
        best_team = team_name

print(best_team)