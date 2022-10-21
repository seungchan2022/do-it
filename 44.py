import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
d = [0] * n     # 노드값 저장 리스트(거리값?)
lcm = 1         # 최소 공배수

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))     # 최소 공배수 갱신

def dfs(v):                         # v = a, i[0] = b ?
    visited[v] = True
    for i in graph[v]:
        next = i[0]
        if not visited[next]:
            d[next] = d[v] * i[2] // i[1]   # 다음 노드값 = 현재 노드값 * 비율
            # ex) 4:1 = 3:1 -> 1*3 = 4*1 -> 1 = 4*1 / 3 => d[v]:d[next] = i[1]:i[2] -> d[next] = d[v]*i[2]//i[1]
            dfs(next)

d[0] = lcm
dfs(0)
mgcd = d[0]     # 모든 노드의 최대 공약수

for i in range(1, n):
    mgcd = gcd(mgcd, d[i])

for i in range(n):
    # 각 노드의 값을 모든 노드의 최대 공약수로 나눈다
    print(int(d[i] // mgcd), end=' ')