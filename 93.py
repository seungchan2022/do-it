# 2342

import sys
input = sys.stdin.readline
INF = int(1e9)

array = list(map(int, input().split()))

# dp[N][L][R]: N개의 수열을 수행했고, 왼쪽이 L 오른쪽이 R에 있을때 최수 누적 힘
dp = [[[INF for k in range(5)] for j in range(5)] for i in range(100001)]

# 한 발을 이동할 때 드는 힘을 미리 저장(mp[1][2]: 1 -> 2로 이동할때 드는 힘)
mp = [[0, 2, 2, 2, 2], [2, 1, 3, 4, 3], [2, 3, 1, 3, 4], [2, 4, 3, 1, 3], [2, 3, 4, 3, 1]]

s = 1   # 수열 수행 횟수
dp[0][0][0] = 0

index = 0   # array의 index

while array[index] != 0:
    n = array[index]
    for i in range(5):
        if n == i:  # 두 발이 같은 자리 X
            continue
        for j in range(5):
            # 오른발을 옮겨 현재 모습이 됐을때 최소 저장
            dp[s][i][n] = min(dp[s - 1][i][j] + mp[j][n], dp[s][i][n])
    
    for j in range(5):
        if n == j:  # 두 발이 같은 자리 X
            continue
        for i in range(5):
            # 왼발을 옮겨 현재 모습이 됐을때 최소 저장
            dp[s][n][j] = min(dp[s - 1][i][j] + mp[i][n], dp[s][n][j])

    s += 1
    index += 1

s -= 1  # 마지막 이동 횟수로 index 조정
result = INF

for i in range(5):
    for j in range(5):
        result = min(result, dp[s][i][j])   # 모두 수행한 후 최솟값 찾기

print(result)


"""
dp[N][L][R]: N개의 수열을 수행했고, 왼쪽이 L 오른쪽이 R 위치에 있을때 최수 누적 힘
mp[i][j]: i -> j로 이동하는데 드는 힘

# 왼발 이동          현재 왼발 위치: i + i -> L 위치로 이동
    dp[N][L][R] = mind(dp[N - 1][i][R] + mp[i][L], dp[N][L][R])

# 오른발 이동      현재 오른발 위치: i + i -> R 위치로 이동
    dp[N][L][R] = mind(dp[N - 1][L][i] + mp[i][R], dp[N][L][R])
"""

----------------------------------------------------------------------------------------------

import sys
input = sys.stdin.readline
INF = int(1e9)

array = list(map(int, input().split()))

d = [[[INF for k in range(5)] for j in range(5)] for i in range(100001)]

# mp[i][j]: i -> j로 이동했을떄 드는 힘
mp = [[0, 2, 2, 2, 2], [2, 1, 3, 4, 3], [2, 3, 1, 3, 4], [2, 4, 3, 1, 3], [2, 3, 4, 3, 1]]

s = 1   # 수열 수행 횟수
index = 0   # array의 index

d[0][0][0] = 0

while array[index] != 0:
    n = array[index]    # 수열 값(발이 위치해야 할 곳)
    
    for i in range(5):
        if n == i:  # 두 발이 같은 곳 X
            continue
        for j in range(5):
            # 오른발 옮기기 j -> n
            d[s][i][n] = min(d[s - 1][i][j] + mp[j][n], d[s][i][n])

    for j in range(5):
        if n == j:  # 두 발이 같은 곳 X
            continue
        for i in range(5):
            # 왼발 옮기기 i -> n
            d[s][n][j] = min(d[s - 1][i][j] + mp[i][n], d[s][n][j])

    s += 1
    index += 1

result = INF

for i in range(5):
    for j in range(5):
        result = min(result, d[len(array) - 1][i][j])

print(result)
