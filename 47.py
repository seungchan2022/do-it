# 1325

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)    # 거리 값 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(x):
    # 모든 노드에 대해서 탐색 해야 되므로 탐색 할때마다 방문 리스트를 초기화 해주어야 된다
    # 함수 밖에서 선언 하면 할때마다 초기화 해주어야 된다
    visited = [False] * (n + 1)     
    visited[x] = True
    q = deque()
    q.append(x)

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True   # 방문 처리
                distance[i] += 1    # 거리값 갱신
                q.append(i)

for i in range(1, n + 1):
    bfs(i)

temp = 0        # 최대값 찾을 변수

for i in range(1, n + 1):
    temp = max(temp, distance[i])

for i in range(1, n +1):
    if temp == distance[i]:
        print(i, end=' ')
