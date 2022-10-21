# 11657

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = []      # 모든 간선에 대한 정보 리스트
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 경우가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 갱신되면 음수 순환 존재
                if i == n - 1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])