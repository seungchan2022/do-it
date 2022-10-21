# 11505

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
treeHeight = 0      # 트리의 높이
length = n      # 리프 노드의 개수
mod = 1000000007

while length != 0:
    length //= 2
    treeHeight += 1

treesize = pow(2, treeHeight + 1)   
leftNodeStartIndex = treesize // 2 - 1  # 리포 노드의 개수
tree = [1] * (treesize + 1)     # 곱하기이므로 초깃값 1로 설정

for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

def setTree(i):
    while i != 1:
        tree[i // 2] *= tree[i] % mod   # 나머지 연산 후 저장
        i -= 1

setTree(treesize - 1)

# 값 변경 함수
def changeVal(index, value):
    tree[index] = value     # 현재 index 위치에 신규 변경 값 저장
    while index > 1:
        index //= 2
        # 부모 노드에 두 자식 노드값을 곱하고 나머지 연산 후 저장
        tree[index] = tree[index * 2] % mod * tree[index * 2 + 1] % mod
    
# 구간 곱 계산 함수
def getSum(s, e):
    partsum = 1
    while s <= e:
        if s % 2 == 1:
            partsum *= tree[s] % mod
            s += 1
        if e % 2 == 0:
            partsum *= tree[e] % mod
            e -= 1
        s //= 2
        e //= 2
    return partsum

for i in range(m + k):
    q, s, e = map(int, input().split())
    if q == 1:
        changeVal(leftNodeStartIndex + s, e)
    elif q == 2:
        s += leftNodeStartIndex
        e += leftNodeStartIndex
        print(getSum(s, e))