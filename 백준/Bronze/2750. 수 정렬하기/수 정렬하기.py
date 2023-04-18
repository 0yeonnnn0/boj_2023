N = int(input())
data = []

for i in range(N):
    num = int(input())
    data.append(num)

data.sort(reverse=True)
for i in range(N):
    print(data.pop())