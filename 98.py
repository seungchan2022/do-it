# 17387

import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# CCW함수
def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    return 0

# 선분 겹침 여부 판별 함수(두 선분이 일직선에 있을 경우 판별 방법)
def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        return True
    return False

# 선분 교차  판별 함수
def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)
    if abc * abd == 0 and cda * cdb == 0:   # 두 선분이 일직선 일때
        return check(x1, y1, x2, y2, x3, y3, x4, y4)    # 겹치는 선분인지 판별
    elif abc * abd <= 0 and cda * cdb <= 0: # 선분이 교차하는 경우(CCW 결괏값의 곱이 모두 양수가 아닌 경우)
        return True
    return False

result = cross(x1, y1, x2, y2, x3, y3, x4, y4)

if result:
    print(1)
else:
    print(0)