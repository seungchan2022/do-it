# 1854

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[INF] * k for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start][0] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now][k - 1] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 새로운 총 거리 < 새로운 노드의 k번째 최단 거리
            if cost < distance[i[0]][k - 1]:
                distance[i[0]][k - 1] = cost        # 저장을 하고
                distance[i[0]].sort()               # 배열
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

for i in range(1, n + 1):
    if distance[i][k - 1] == INF:
        print(-1)
    else:
        print(distance[i][k - 1])

        
"""
k번째 최단 경로 해결 방법
-> 최단 경로를 표현하는 리스트를 k개의 행을 갖는 2차원 리스트의 형태로 변경 하면
    최단 경로 ~ k번째 최단 경로까지 표현 가능

최단 거리 리스트 채우기 규칙
-> 연결 노드의 k번재 경로와 신규 경로를 비교해 신규 경로가 더 작을때 갱신
    이때 경로가 갱신되는 경우 거리 배열을 오름 차순으로 정렬하고 우선순위 큐에 추가
    (맨 마지막 배열에 저장 -> 정렬 -> 우선순위큐 push)
"""