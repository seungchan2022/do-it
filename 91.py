# 1915

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# dp[i][j]: i,j 위치에서 왼쪽 위로 만들 수 있는 최대 정사각형 길이를 저장하는 리스트
dp = [[0] * (m + 1) for _ in range(n + 1)]

result = 0  # 최대값 저장 변수

for i in range(n):
    data = list(input())
    for j in range(m):
        dp[i][j] = int(data[j])
        if dp[i][j] == 1 and i > 0 and j > 0:
            dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        result = max(result, dp[i][j])

print(result * result)

-----------------------------------------------------

n, m = map(int, input().split())

dp = []
for _ in range(n):
    dp.append(list(map(int, input())))

result = 0

for i in range(n):
    for j in range(m):
        if dp[i][j] == 1 and i > 0 and j > 0 :
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
        result = max(result, dp[i][j])

print(result * result)
