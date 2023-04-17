X = []


for i in range(10):
    n = int(input())
    X.append(n%42)
X = set(X)
print(len(X))