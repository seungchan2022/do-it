# 1256

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

array = [[1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 모든 경우의 수는 "a" or "z"로 끝난다
        # 즉, (n - 1) + m + "a" or n + (m - 1) + "z"로 된다
        array[i][j] = array[i - 1][j] + array[i][j - 1]

if array[n][m] < k:
    print(-1)
else:
    result = ""
    while True:
        if n == 0 or m == 0:
            result += "a" * n
            result += "z" * m
            break
        
        # 기준은 "a"로 시작 하는가 
        flag = array[n - 1][m]
        if k <= flag:   # k번째 수는 "a"로 시작
            result += "a"
            n -= 1
        else:       # k번째 수는 "z"로 시작
            result += "z"
            m -= 1
            k -= flag
    print(result)


"""
if k <= array[i - 1][j]: -> k번째 수는 "a"로 시작
else: k번째 수는 "z"로 시작, 이때 k -= flag를 해줘야 한다!
k번째 수도, 사전순으로 k번째 수였으므로, k가 z로 시작하면, k-= flag를 해야 한다
ex) n = 2, m = 2, k = 5일때, k는 3보다 크므로, k는 z시작한다
하지만, z로 시작 하는 것중에 5번째는 없다.
즉, "z"로 시작한다면, 앞의 a로 시작하는 경우의수는 빼줘야 한다

"""

# https://dailymapins.tistory.com/136?category=1017255