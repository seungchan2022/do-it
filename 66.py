# 1414

import sys
input = sys.stdin.readline

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

n = int(input())
parent = [i for i in range(n + 1)]

data = []   # 인접 행렬 형태로 들어오는 데이터를 변형하기 위한 리스트
edges = []
total = 0   # 전체 랜선
result = 0  # 크루스칼 비용

for i in range(n):
    data.append(list(input()))
    for j in range(n):
        if data[i][j] == 0:
            edges.append((0, i + 1, j + 1))
        else:
            if ord('a') <= ord(data[i][j]) <= ord('z'):
                edges.append((ord(data[i][j]) - ord('a') + 1, i + 1, j + 1))
                total += ord(data[i][j]) - ord('a') + 1
            elif ord('A') <= ord(data[i][j]) <= ord('Z'):
                edges.append((ord(data[i][j]) - ord('A') + 27, i + 1, j + 1))
                total += ord(data[i][j]) - ord('A') + 27

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

check = True
for i in range(1, n + 1):
    # 모든 컴퓨터가 연결되어있지 않으면
    if find_parent(parent, i) != 1:
        check = False

if check:
    print(total - result)
else:
    print(-1)