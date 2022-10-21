# 1976    

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())    # 도시 개수
m = int(input())    # 여행 경로 데이터
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

graph = []
data = []   # union 연산을 할 데이터
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            data.append((i + 1, j + 1))

plans = list(map(int, input().split()))

# 주어진 연결 여부 정보를 하나씩 union 연산
for i in range(len(data)):
    a, b = data[i]
    union_parent(parent, a, b)

result = True
# 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plans[i]) != find_parent(parent, plans[i + 1]):
        result = False

if result:
    print('YES')
else:
    print('NO')