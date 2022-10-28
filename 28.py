# 1167

from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, len(data) - 1, 2):
        graph[data[0]].append((data[j], data[j + 1]))

# visited = [-1] * (n + 1)

def bfs(start):
    # 탐색을 여러 번 수행할 때 이렇게 함수 안에 넣지 않고 밖에서 선언 하면 탐색 할때 마다 방문 리스트를 선언 해주어야 한다
    visited = [-1] * (n + 1)    # 방문 여부: -1 이면 방문 X
    q = deque()
    q.append(start)
    visited[start] = 0
    answer = [0, 0]     # 거리가 가장 먼 트리의 지름과 노드 저장(거리, 노드)
    while q:
        v = q.popleft()
        for e, d in graph[v]:
            if visited[e] == -1:    # 아직 방문하지 않았다면
                visited[e] = visited[v] + d     # 방문 처리
                q.append(e)
                # 현재 노드로부터 가장 거리가 먼 노드의 번호로 거리 갱신
                if visited[e] > answer[0]:      # 최댓값 구하기
                    answer = visited[e], e      # (거리, 노드)
    return answer

distance, node = bfs(1)     # 아무 노드나 설정
# visited = [-1] * (n + 1) 
distance, node = bfs(node)
print(distance)



"""
1: 트리의 지름: 가장 먼 두 노드 사이의 거리
2: 선형 시간 안에 트리의 지름 구하는 방법
    1) 트리에서 임의의 노드 X 설정
    2) 노드 X를 기준으로 가장 먼 노드 Y 탐색
    3) 노드 Y를 기준으로 가장 먼 노드 Z 탐색
    4) 트리의 지름: 노드 Y와 노드 Z 사이의 거리
"""


"""
DFS 풀이

import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)    # 탐색 여부, 간선 거리
visited[1] = 0

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, len(data) - 2, 2):
        graph[data[0]].append((data[j], data[j + 1]))

def dfs(x, y):
    for a, b in graph[x]:
        if visited[a] == -1:    # 탐색하지 않은 노드라면
            visited[a] = b + y
            dfs(a, b + y)

dfs(1, 0)   # 1번 노드 부터 시작

start = visited.index(max(visited))     # 1번 노드에서 가장 먼 노드 번호 찾기
visited = [-1] * (n + 1)        # 새로 탐색 하면 거리 리스트 초기화 해줘야 됨
visited[start] = 0
dfs(start, 0)       # 1번 노드와 가장 먼 노드인 start에서 다시 제일 먼 노드 찾기

print(max(visited))


풀이 방법
    1: DFS를 통해 첫번째 노드에서 가장 먼 노드 찾기
    2: 첫번째 노드에서 가장 먼 노드를 시작으로 다시 가장 먼 노드 찾기
"""
