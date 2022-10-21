# 1991

import sys
input = sys.stdin.readline

n = int(input())
tree = dict()   # tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회(현재노드 -> 왼쪽 -> 오른쪽)
def preorder(now):
    if now == '.':
        return
    print(now, end='')          # 1. 현재 노드
    preorder(tree[now][0])      # 2. 왼쪽
    preorder(tree[now][1])      # 3. 오른쪽

# 중위 순회(왼쪽 -> 현재 -> 오른쪽)
def inorder(now):
    if now == '.':
        return
    inorder(tree[now][0])       # 1. 왼쪽
    print(now, end='')          # 2. 현재 노드
    inorder(tree[now][1])       # 3. 오른쪽

# 후위 순회(왼쪽 -> 오른쪽 -> 현재)
def postorder(now):
    if now == '.':
        return
    postorder(tree[now][0])     # 1. 왼쪽
    postorder(tree[now][1])     # 2. 오른쪽
    print(now, end='')          # 3. 현재 노드

preorder('A')
print()
inorder('A')
print()
postorder('A')