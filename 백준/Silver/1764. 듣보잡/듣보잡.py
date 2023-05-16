import sys
input = sys.stdin.readline          #시간초과 꿀팁

n, m = map(int, input().split())
ddmt = {}
ddbd = {}

for i in range(n):
    name = input()
    ddmt[name] = True

for i in range(m):
    name = input()
    if name in ddmt:
        ddbd[name] = True

ddbdmt = sorted(ddbd)

print(len(ddbd))
for name in ddbdmt:
    print(name, end="")