# 1747

import math

n = int(input())
a = [0] * (10000001)

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a)) + 1)):
    if a[i] == 0:
        continue
    for j in range(i + i, len(a), i):
        a[j] = 0

# 팰린드롬 수 판별 함수
def check(target):
    data = list(str(target))    # 숫자 값을 비교하기 위해 리스트 형태로 변환
    # 투 포인터 알고리즘 사용
    s = 0
    e = len(data) - 1
    while s < e:
        if data[s] != data[e]:
            return False
        s += 1
        e -= 1
    return True

i = n
while True:     # n부터 1씩 증가시키면서 소수이면서 팰린드롬 수인지 판별
    if a[i] != 0:
        if check(a[i]):
            print(a[i])
            break
    i += 1