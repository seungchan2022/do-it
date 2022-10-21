# 1016

import math

min, max = map(int, input().split())
check = [False] * (max - min + 1)

for i in range(2, int(math.sqrt(max) + 1)):
    pow = i * i     # 제곱수
    start_index = int(min / pow)    # 최솟값 / 제곱수 (단, 나머지가 0이 아니면 1을 더함 -> 다음 수 확인)
    if min / pow != 0:
        start_index += 1
    # 제곱수의 배수 형태로 탐색
    for j in range(start_index, int(max / pow) + 1):
        check[int((j * pow) - min)] = True  # 제곱수를 True로 변경(check 안에 있는것은 index)

count = 0   # 제곱수가 아닌 수를 카운트할 변수

for i in range(max - min + 1):
    if not check[i]:
        count += 1

print(count)