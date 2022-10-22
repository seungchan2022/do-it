import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # dp의 범위가 n + 1 이므로 => a[i][j] (X)
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + a[i - 1][j - 1]

for i in range(m):  
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 -1][y1 - 1]
    print(result)

"""
예를 들어 (2, 2) ~ (3, 4)구간 합을 구하려면, (3, 4)구간 합에서  - (1, 4)구간 합 - (3, 1)구간 합 + (1, 1) (중복해서 뺀 값)
"""
