# 1016

import math

min, max = map(int, input().split())

# min ~ max 사이에 제곱수 판별 리스트
check = [False] * (max - min + 1)

for i in range(2, int(math.sqrt(max)) + 1):
    pow = i * i     # 제곱 수
    start_index = int(min / pow)    # 최솟값 / 제곱수
    # 단, 나머지가 있는 경우 1을 더해 min보다 큰 제곱수에서 시작하도록 설정
    if min / pow != 0:
        start_index += 1
    # 제곱수의 배수 형태로 탐색
    for j in range(start_index, int(max / pow) + 1):
        check[int((j * pow) - min)] = True  # 제곱수를 True로 변경(check 안에 있는 것은 index)

count = 0   # 제곱수가 아닌 수를 카운트할 변수

for i in range(len(check)):
    if check[i] == False:
        count += 1

print(count)
