# 11437(74), 11438(75)

# 최소 공통 조상(LCA)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21

n = int(input())
parent = [[0] * LOG for _ in range(n + 1)]    # 부모 노드 정보
d = [0] * (n + 1)   # 각 노드까지의 깊이
c = [False] * (n + 1)   # 각 노드의 깊이가 계산 되었는지 여부
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth    # 매번 노드에 대해 깊이 기록
    for y in graph[x]:  # 인접노드 확인
        if c[y]:    # 이미 깊이를 구했으면
            continue
        parent[y][0] = x    # 한 칸위에 있는 부모에 대한 정보만 먼저 구함
        dfs(y, depth + 1)

# 전체 부모관계를 설정하는 함수
def set_parent():
    dfs(1, 0)   # 루트노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n +1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# A와 B의 최소 공통 조상 구하는 함수
def lca(a, b):
    # b가 더 작도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이가(depth) 동일하므로
    # 큰 크기부터 작은 크기까지 차례대로 확인하면서 값 줄이기 (ex) 15: 8 -> 4 -> 2 -> 1
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]    # 더 깊은 쪽의 길이가 줄어들도록
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
