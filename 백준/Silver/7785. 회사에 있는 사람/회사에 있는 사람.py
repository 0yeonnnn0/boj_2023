import sys
input = sys.stdin.readline

n = int(input())
worker = {}

for i in range(n):
    A, B = map(str, input().split())
    if B == "enter":
        worker[A] = True
    else:
        del worker[A]

namelist = sorted(worker, reverse=True)

for A in namelist:
    print(A)