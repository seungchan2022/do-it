# 1043

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


n, m = map(int, input().split())    # 사람수, 파티수
true = list(map(int, input().split()))  # 진실을 아는 사람 데이터
t = true[0]     # 진실을 아는 사람 수
del true[0]
result = 0

party = []
for i in range(m):
    party.append(list(map(int, input().split())))
    del party[i][0]

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a = party[i][0]     # i번째 파티의 1번째 사람
    for j in range(1, len(party[i])):   # i번째 파티의 사람 수만큼 반복
        union_parent(parent, a, party[i][j])    # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기

for i in range(m):
    check = True
    a = party[i][0]     
    for j in range(len(true)):  # 진실을 아는 사람들의 수만큼 반복
        # 각 파티의 루트 노드와 진실을 아는 사람들의 루트 노드가 같다면 과장할 수 X
        if find_parent(parent, a) == find_parent(parent, true[j]):
            check = False
            break
    # 모든 다른 경우
    if check:
        result += 1

print(result)


"""
파티에 참석한 사람들을 1개의 집합으로 생각하고, 각각의 파티마다 union연산을 이용해 사람들을 연결
find연산을 이용해 각 파티의 루트 노드와 진실을 아는 사람들이 같은 그룹에 있는지 확인
"""