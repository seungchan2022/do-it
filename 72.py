# 10868

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
treeHeight = 0      # 트리의 높이
length = n      # 리프 노드의 개수

# 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length != 0:
    length //= 2
    treeHeight += 1

treesize = pow(2, treeHeight + 1)
leftNodeStartIndex = treesize // 2 - 1  # 리프 노드의 시작 인덱스
tree = [INF] * (treesize + 1)   # 최솟값을 찾을 것이므로 tree리스트를 무한으로 초기화

# tree 리스트에 리프 노드 영역 데이터 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:   # 인덱스가 루트가 아닐 때 까지
        # 부모 노드와 현재 노드 값 비교
        if tree[i // 2] > tree[i]:  # 부모 노드 > 현재 노드
            tree[i // 2] = tree[i]  # 현재 노드값을 부모 노드에 저장
        i -= 1

setTree(treesize - 1)

# 최솟값 계산 함수
def getMin(s, e):
    min_value = INF
    while s <= e:
        if s % 2 == 1:
            min_value = min(min_value, tree[s])
            s += 1
        if e % 2 == 0:
            min_value = min(min_value, tree[e])
            e -= 1
        s //= 2
        e //= 2
    return min_value

for _ in range(m):
    s, e = map(int, input().split())
    s += leftNodeStartIndex     # tree에서 시작 인덱스
    e += leftNodeStartIndex     # tree에서 종료 인덱스
    print(getMin(s, e))