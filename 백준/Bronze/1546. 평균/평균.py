N = int(input())
feList = list(input().split())
feList = [int(i) for i in feList]
feList.sort(reverse=True)
highScore = feList[0]
for i in range(0, N):
    feList[i] = feList[i]/highScore*100


print(sum(feList)/N)