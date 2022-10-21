# 1948 (임계경로: 여러가지 경로중에서 가장 긴 시간이 걸리는 경로)

import sys
input = sys.stdin.readline

from collections import deque


n = int(input())
m = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
# 역추적 bfs를 이용하기 위해 역방향 인접 리스트 생성
r_graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    r_graph[b].append((a, c))   # 역방향 간선 정보 저장
    indegree[b] += 1

start, end = map(int, input().split())      # 시작 도시, 도착 도시

def topology_sort():
    result = [0] * (n + 1)  # 결과 리스트
    check = [0] * (n + 1)   # 중복 체크 리스트(역추적 BFS 과정에서 정점 방문 여부를 기록하는 이유는 이후의 중복 카운팅을 막기 위해서이다. 그렇다고 방문한 정점으로의 간선을 카운팅하지 않으면 안 된다)
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for i, j in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + j) # (타깃 노드의 현재 경로값, 현재 노드의 경로값 + 도로 시간값)
            if indegree[i] == 0:
                q.append(i)

    # 백 트래킹
    count = 0   # 1분도 쉬지 않고 달려야 하는 도로의 수(임계 경로의 수)
    q.append(end)
    while q:    # 도착점에서 시작점으로
        now = q.popleft()
        for i, j in r_graph[now]:
            # 도착점까지의 비용에서 시작점의 비용을 뺐을 때 그 간선비용과 같다면
            if result[now] - result[i] == j:
                count += 1
                if check[i] == 0:   # 큐에 한번씩만 담을 수 있도록, 중복 방문 제거
                    q.append(i)
                    check[i] = 1

    print(result[end])
    print(count)

topology_sort()


"""
어떤 사람은 이 시간에 만나기 위하여 1분도 쉬지 않고 달려야 한다.=> 임계경로
임계경로는 전체 중에서 여러 경로가 동시에 이루어질 때, 가장 오래 걸리는 경로를 의미한다. 
가장 오래 걸리는 경로를 구하고 백트래킹을 할 때 중복된 도로를 제거해주어야한다
1->2 2->6 6->7 // 1->4 4->6 6->7 의 두가지 경우가 존재한다.
6->7은 중복된 도로이므로 한 번만 카운트 해주어야 한다 
"""