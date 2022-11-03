# 1707

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1 # 시작점 그룹은 1로

    while q:
        v = q.popleft() # 현재 정점
        for i in graph[v]: # 현재 정점과 연결된 정점이
            if visited[i] == 0: # 방문하지 않았다면 현재 정점과 다른 그룹으로 지정
                q.append(i)
                visited[i] = -visited[v]
            elif visited[i] == visited[v]: # 이미 방문한 정점이 같은 그룹이라면 False
                return False
    return True

for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)] # 연결 리스트
    visited = [0] * (v + 1) # 방문한 정점 체크
    result = True # 이분그래프 여부

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            if not bfs(i): # 이분 그래프가 아니라면 탐색 중단
                result = False
                break
    
    if result:
        print('YES')
    else:
        print('NO')

"""
1. 필요한 정보를 입력받은 뒤 방문한 정점을 체크할 수 있는 visited와 이분그래프인지 확인할 수 있는 변수 result를 생성한다.

2. 모든 정점을 탐색한다.

    2-1. 아직 방문하지 않은 정점이라면 bfs를 수행한다.

    2-2. 시작점은 그룹을 1로 만들어주고 큐를 탐색한다.

    2-3. 현재 정점과 연결된 정점들을 가져와 연결된 정점을 방문하지 않았다면 다른 그룹으로 지정한다. 

    2-4. 연결된 정점이 이미 방문했고 현재 정점과 같은 그룹이라면 False를 리턴한다. (같은 그룹(=색상)인데 간선이 있는 것이므로)

    2-5. bfs 수행 결과가 False 라면 이분그래프가 아니므로 탐색을 중단한다.

3. 결과에 따른 출력을 해준다.
"""

# https://soohyun6879.tistory.com/242
