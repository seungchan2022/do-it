# 1916

import heapq
import sys
sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start, end):
    q = []
    # 시작 노드 0으로 설정하고 큐에 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))   # (거리, 노드)

    while q:
        # 가장 최단거리가 짧은 노드 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 처리 된적이 있으면 무시
        if distance[now] < dist:
            continue
        # 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 가는 비용이 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]

print(dijkstra(start, end))