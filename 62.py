# 11403

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            # a -> k -> b로 가는 길이 있다면
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()