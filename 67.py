# 11725

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
visited = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)  # 부모 노드를 저장할 정답 리스트

# 트리의 간선의 개수: 노드의 개수 - 1
for _ in range(1, n): 
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = True
    # 인접 노드 확인
    for i in tree[v]:
        # 아직 방문 하지 않았으면
        if not visited[i]:
            # 미 방문 노드의 부모노드로 현재 노드 저장
            answer[i] = v   # 부모 노드 저장
            dfs(i)  # dfs(미 방문 노드)

dfs(1)

for i in range(2, n + 1):
    print(answer[i])