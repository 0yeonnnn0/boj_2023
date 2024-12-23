def count_love(name):
    return {char: name.count(char) for char in 'LOVE'}

yundoo_name = input()
yundoo_love = count_love(yundoo_name)
N = int(input())
results = []

for _ in range(N):
    team_name = input()
    team_love = count_love(team_name)
    L = yundoo_love['L'] + team_love['L']
    O = yundoo_love['O'] + team_love['O']
    V = yundoo_love['V'] + team_love['V']
    E = yundoo_love['E'] + team_love['E']
    winning_prob = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    results.append((team_name, winning_prob))
results.sort(key=lambda x: (-x[1], x[0]))
print(results[0][0])