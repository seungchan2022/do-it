# 에라토스테네스의 체 알고리즘(여러개의 수가 소수인지 아닌지 판별할 때 사용)

import math

m, n = map(int, input().split())    # m ~ n 까지의 모든 수에 대해 소수 판별
# 처음에는 모든 수가 소수(True)인 것으로 초기화(0, 1 제외)
array = [True for _ in range(n + 1)]
array[1] = False

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱급 까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n) + 1)):
    if array[i] == True:    # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수 지우기
        j = 2   # i의 배수를 찾을 변수
        while i * j <= n:
            array[i * j] = False
            j += 1


# m ~ n까지 소수 출력
for i in range(m, n + 1):
    if array[i]:        # 소수 인것만 출력
        print(i)

        
"""
가끔 '1'이 소수인지 판별해야 하도록 입력조건이 주어지면,
1은 소수가 아니므로 array[1]의 값으로 False를 넣어주는 부분을 추가하면 된다.
"""


"""
에라토스테네스의 체 원리

1: 구하고자 하는 소수의 범위만큼 1차원 리스트 생성
2: 2부터 시작하고 현재 숫자가 지워진 상태가 아닌 경우 현재 선택된 숫자의 배수에 해당하는 수를 리스트에서 끝까지 탐색하면서 지운다.
    이때 처음으로 선택된 숫자는 지우지 않는다.
3: 리스트 끝까지 2를 반복한 후 리스트에 남아 있는 모든 수 출력
"""

import math

m, n = map(int, input().split())

# 소수가 아닌수를 0값으로 둔다.
a = [0] * (n + 1)

for i in range(1, n + 1):
    a[i] = i    # 각각의 인덱스 값으로 초기화

a[1] = 0        # 1은 소수 X

for i in range(2, int(math.sqrt(n)) + 1):   # 제곱근까지만 수행
    if a[i] == 0:   # 소수가 아니면 넘어감
        continue
    for j in range(i + i, n + 1, i):    # 배수 지우기
        a[j] = 0

for i in range(m, n + 1):
    if a[i] != 0:
        print(a[i])

        
