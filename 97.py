# 17387

import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if temp < 0:    # 시계
        return -1
    elif temp > 0:  # 반시계
        return 1
    return 0    # 일직선

print(ccw(x1, y1, x2, y2, x3, y3))