# 1043

# 특정 원소가 속한 집합 찾기
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())    # n:사람수, m:파티수
true = list(map(int, input().split())) # 진실을 아는 사람수, 그 사람의 대한 번호
t = true[0] # 진실을 아는 사람수
del true[0]
result = 0

party = []  # 각 파티에 대한 정보 담을 리스트
for i in range(m):
    party.append(list(map(int, input().split())))
    del party[i][0]     # 각 파티에 첫 번째원소(사람수) 삭제

parent = [i for i in range(n + 1)]

for i in range(m):
    a = party[i][0]     # i번째 파티의 1번째 사람
    for j in range(1, len(party[i])):   # i번째 파티의 사람 수 만큼 반복(len(party[i]): 각각의 파티의 길이)
        union(parent, a, party[i][j])   # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기

for i in range(m):
    check = True
    a = party[i][0]
    for j in range(len(true)):    # 진실을 아는 사람 수 만큼 반복
        # 각 파티의 루트 노드와 진실을 아는 사람들의 루트 노드가 같다면 과장 할 수 X
        if find(parent, a) == find(parent, true[j]):
            check = False
            break
    # 모두 다른 경우
    if check:
        result += 1

print(result)


"""
파티에 참석한 사람들을 1개의 집합으로 생각하고, 각각의 파티마다 union연산을 이용해 사람들을 연결
find연산을 이용해 각 파티의 루트 노드와 진실을 아는 사람들이 같은 그룹에 있는지 확인
"""
