# 11049

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
data = []   # 행렬 저장 리스트

dp = [[-1] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    r, c = map(int, input().split())
    data.append((r, c))

def execute(s, e):   # s: 시작 행렬 index, e: 종료 행렬 index
    result = INF
    if dp[s][e] != -1:  # 이미 계산 했다면
        return dp[s][e]
    if s == e:          # 행렬 1개일 때
        return 0
    if s + 1 == e:      # 행렬이 2개 일때
        return data[s][0] * data[e][0] * data[e][1]
    for i in range(s, e):   # 행렬이 3개 이상 일때
        # dp[s][e] = dp[s][i] + dp[i + 1][e] + a(s행렬의 row * (i + 1)행렬의 row * e 행렬의 column)
        result = min(result, execute(s, i) + execute(i + 1, e) +  data[s][0] * data[i + 1][0] * data[e][1])
    dp[s][e] = result   # 가장 최솟값 저장
    return dp[s][e]

print(execute(0, n - 1))

"""
dp의 특징 중 하나가 부분문제를 구해 큰 문제를 해결하는 것이다.
따라서 점화식을 구하기 막막할때 부분문제가 해결됐다고 가정하고, 점화식을 떠올려 볼것!
"""
