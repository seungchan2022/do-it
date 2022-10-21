# 유클리드 호제법을 이용한 gcd(최대 공약수) 찾기
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, b % a)    # 재귀함수 형태

a, b = map(int, input().split())
result = gcd(a, b)

while result > 0:
    print(1, end='')
    result -= 1

# 11 ~ 13 => print('1'*result)

"""
import math

a, b = map(int, input().split())
print('1'*math.gcd(a, b))


a, b의 최대공약수 만큼 1을 출력하면 된다.
"""