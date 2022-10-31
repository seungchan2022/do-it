# 11689
# 오일러 피함수(1부터 n까지 범위에서 n과 서로소인 자연수의 개수)


import math

n = int(input())
result = n

for p in range(2, int(math.sqrt(n)) + 1):   # 제곱근까지만 진행
    if n % p == 0:  # p(현재 값)가 소인수이면
        result -= result / p    # 결과값 갱신
        while n % p == 0:   # 2^7 * 11 이라면 11만 남김
            n /= p

# 반복문 종료 후 현재 n이 1보다 크면 n이 마지막 소인수 라는 뜻이므로 result값을 마지막으로 갱신
if n > 1:   # 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / n

print(int(result))
