# 13023

import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

n, m = map(int, input().split())    # 노드, 간선
graph = [[] for _ in range(n)]
visited = [False] * n
result = False          # 깊이가 5까지 갔는지에 대한 확인 변수

# 간선 정보
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, depth):      # v: 현재 노드, depth: 깊이
    global result
    if depth == 5:      # 깊이가 5가 되면 종료(서로 연결된 간선이 4개 이상 연결 되면)
        result = True
        return 
    visited[v] = True   # 현재 노드 방문 처리
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth + 1)   # 재귀 호출마다 깊이 증가
    visited[v] = False  # 이해 X            


for i in range(n):
    dfs(i, 1)   # 노드마다 dfs실행
    if result:  # depth가 5에 도달한 적이 있다면
        break

if result:
    print(1)
else:
    print(0)