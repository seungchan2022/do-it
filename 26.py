# 1260

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()     # 번호가 작은 노드 부터 방문하기 위해 정렬

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (n + 1)
dfs(graph, v, visited)

# bfs
from collections import deque

def bfs(graph, v, visited):
    q = deque([v])        # q = deque() / q.append(v), q = deque(v) (X)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

print()
visited = [False] * (n + 1)
bfs(graph, v, visited)