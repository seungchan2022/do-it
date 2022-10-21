import heapq
import sys

n = int(input())
q = []
for i in range(n):
    a = int(input())
    if a != 0:
        # 힙에 값을 넣을 떄(절댓값, 원래값)형태로 넣어줌으로써 절대값을 기준으로 정렬
        heapq.heappush(q, (abs(a), a))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])

"""
heapq.heappush(q, (a, b))   -> (우선순위, 값)
"""