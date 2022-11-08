# 1389

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min = INF
answer = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        count += graph[i][j]
    if min > count:     # 가장 작은 값을 지닌 i 찾기
        min = count
        answer = i

print(answer)



"""
25 ~ 36
(두가지 다 알아두기)
result = []

for a in range(1, n + 1):
    temp = 0
    for b in range(1, n + 1):
        temp += graph[a][b]
    result.append((temp, a))
        
result = sorted(result, key=lambda x: (x[0], x[1]))
print(result[0][1])
"""
