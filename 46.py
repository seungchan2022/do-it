# 18352

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

result = []     # 거리가 같은 노드들 담을 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    q = deque()
    visited[v] += 1
    q.append(v)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

bfs(x)

for i in range(1, n + 1):
    if visited[i] == k:
        result.append(i)

for i in result:
    if not result:
        print(-1)
    else:
        print(i)


"""
최초에는 방문 도시가 1이고, 이동하지 않았으므로 방문 리스트에 0을 저장
이후 방문하는 도시는 이전 도시의 방문 리스트 값 + 1을 방문 리스트에 저장하는 방식으로 이동 거리 저장
"""