# 유클리드 호제법을 이용한 gcd(최대 공약수) 찾기
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, b % a)    # 재귀함수 형태

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)  # lcm(최소 공배수): a * b / gcd(최대 공약수)
    print(int(result))

------------------------------------------------------------

for tc in range(int(input())):
    a, b = map(int, input().split())
    
    # 최대 공약수
    def gcd(a, b):
        while b > 0:
            a, b = b, a%b
        return a
    
    # 최소 공배수
    def lcm(a, b):
        result = a * b // gcd(a, b)
        return result
    print(lcm(a, b))
    
    
"""
import math

for tc in range(int(input())):
    a, b = map(int, input().split())
    print(math.gcd(a, b))
"""
