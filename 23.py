# 11742

import sys
sys.setrecursionlimit(10000)    # 런타임에러를 일으키지 않기 위해
input = sys.stdin.readline

n, m = map(int, input().split())    # 노드, 간선
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0   # dfs실행 횟수 = 연결 요소 개수

# 간선 정보
for _ in range(m):
    u, v = map(int, input().split())
    # 방향이 없는 그래프 이므로
    graph[u].append(v)
    graph[v].append(u)

# dfs 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(graph, i, visited)

print(count)
