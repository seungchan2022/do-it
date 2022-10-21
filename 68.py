# 1068

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
visited = [False] * n
tree = [[] for _ in range(n)]
answer = 0      # 리프노드의 개수
array = list(map(int, input().split()))

x = int(input())    # 삭제할 노드

for i in range(n):
    if array[i] != -1:
        tree[i].append(array[i])
        tree[array[i]].append(i)
    else:
        root = i    # 루트 노드값 저장

def dfs(v):
    global answer
    visited[v] = True
    count = 0   # 자식 노드의 개수를 세는 변수(리프 노드: 자식 노드의 개수가 0개)
    for i in tree[v]:
        # 미 방문 노드이면서 삭제 노드가 아니면(삭제 노드일때도 탐색 중지)
        if not visited[i] and i != x:   
            count += 1  # 자식 노드 개수 증가
            dfs(i)
    # 자식 노드가 0개 이면 리프노드로 간주
    if count == 0:
        answer += 1

# 만약 삭제할 노드가 루트 노드이면 모든 노드가 사라짐
if x == root:
    print(0)
else:
    dfs(root)
    print(answer)