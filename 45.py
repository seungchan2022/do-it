# 21568 (적으면서 해야 이해)

a, b, c = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 유클리드 호제법 함수 구현(역순 계산)
def Execute(a, b):
    ret = [0] * 2       # x, y
    if b == 0:      # 3 % 1 = 0(나머지) - > 1(a) % 0(b) ~
        # 처음 시작하는 x, y는 이전이 없으므로 1, 0으로 지정
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b      # 현재 보고 있는 몫
    v = Execute(b, a % b)   # 재귀    ?
    # x = y', y = x' - y' * q(몫)
    ret[0] = v[1]       # 역순으로 올라오면서 x, y 계산
    ret[1] = v[0] - v[1] * q
    return ret      # x, y를 return

mgcd = gcd(a, b)    # 최대 공약수

# 만약 c가 최대공약수의 배수가 아니라면
if c % mgcd != 0:
    print(-1)
else:
    # 나머지(b)가 0이 될 때까지 재귀함수 호출
    mok = int(c / mgcd)
    ret = Execute(a, b)
    # 결과 값에 c / 최대 공약수의 값을 곱한후 출력
    print(ret[0] * mok, end=' ')
    print(ret[1] * mok)