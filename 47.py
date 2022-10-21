# 1325

from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)      # 거리 저장 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                q.append(i)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    bfs(i)

max_value = 0
for i in range(1, n + 1):
    max_value = max(max_value, answer[i])

for i in range(1, n + 1):
    if max_value == answer[i]:
        print(i, end=' ')