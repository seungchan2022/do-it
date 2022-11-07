# 1219

import sys
input = sys.stdin.readline
INF = int(1e9)

n, start, end, m = map(int, input().split())
edges = []      # 모든 간선에 대한 정보 리스트
distance = [-INF] * (n + 1)     # 양수 사이클을 확인 할것 이므로

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 각 도시에서 버는 수입
data = list(map(int ,input().split()))

# 출발노드 초기화
distance[start] = data[start]

# 양수 사이클이 전파되도록 충분히 큰 수로 반복
for i in range(n + 51):     # 에지의 업데이트를 n - 1번이 아닌 충분히 큰수(n <= 50)만큼 추가로 돌리면서 갱신
    for j in range(m):
        cur = edges[j][0]
        next_node = edges[j][1]
        cost = edges[j][2]
        if distance[cur] == -INF:   # 출발 노드가 방문하지 않은 노드이면
            continue
        elif distance[cur] == INF:  # 출발 노드가 양수 사이클에 연결된 노드 이면
            distance[next_node] = INF   # 종료 노드를 양수 사이클에 연결된 노드로 갱신
        # 더 많은 돈을 벌 수 있는 새로운 경로가 있는 경우 값 갱신
        # 종료 노드의 값 < 출발 노드의 값 + 도착 도시에서의 수입 - 간선 비용
        elif distance[next_node] < distance[cur] + data[next_node] - cost:
            distance[next_node] = distance[cur] + data[next_node] - cost
            if i >= n - 1:  # ?
                distance[next_node] = INF
                

if distance[end] == -INF:   # 도착 도시가 초깃값이면
    print('gg')         # 도착 불가
elif distance[end] == INF:  # 양수 사이클 -> 무한대로 돈을 벌 수 있을 경우
    print('Gee')
else:
    print(distance[end])
