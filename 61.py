# 11404

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):               # k: 거쳐가는 노드
    for a in range(1, n + 1):           # a: 시작 노드
        for b in range(1, n + 1):       # b: 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()