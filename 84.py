# 1463

import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())

d = [0] * (n + 1)
d[1] = 0

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)


print(d[n])


"""
처음엔 당연스럽게 조건문을 통해 구현했다. (n//3 , n//2 , n-=1 순서대로).

하지만 문제의 테스트케이스인 10이 반례였다.

즉, 단순히 조건문으로 풀게되면 10 - > 5 -> 4 -> 2 -> 1 이지만, 사실 10은

10 -> 9 -> 3 - > 1 으로, n/3보다 n-1을 먼저 해줘야 최소값이 나오게 된다.

따라서 n - 1 연산을 제일 먼저 구현 해주어야 한다.
"""