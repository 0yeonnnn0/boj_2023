yeondoo_name = input()
N = int(input())
max_probability = -1
best_team_name = ''

for _ in range(N):
    team_name = input().strip()
    combined_name = yeondoo_name + team_name
    L = combined_name.count('L')
    O = combined_name.count('O')
    V = combined_name.count('V')
    E = combined_name.count('E')
    probability = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    if probability > max_probability or (probability == max_probability and team_name < best_team_name):
        max_probability = probability
        best_team_name = team_name

print(best_team_name)