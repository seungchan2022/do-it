# 11050
# 조합 구하는 법(이항 계수)

# 다이나믹 프로그래밍 이용
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# dp 테이블 생성
d = [[0] * (n + 1) for _ in range(n + 1)]

# dp 테이블 초기화
for i in range(n + 1):
    d[i][0] = 1     # 3C0
    d[i][1] = i     # 3C1
    d[i][i] = 1     # 3C3

# 점화식으로 dp 테이블 값 채우기
for i in range(2, n + 1):
    for j in range(1, i):   # 총 개수 보다 선택 수가 더 클수 X
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

print(d[n][k])

"""
# 재귀
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))

# 반복문
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))
"""