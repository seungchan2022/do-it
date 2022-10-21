# 1722

import sys
input = sys.stdin.readline

f = [0] * 21    # 자리별로 만들 수 있는 경우의 수 저장하기 -> 팩토리얼 형태
s = [0] * 21    # 순열을 담는 리스트
visited = [False] * 21      # 숫자 사용 여부 저장 리스트
n = int(input())
f[0] = 1

# f 리스트 초기화(팩토리얼 초기화) -> 각 자릿수에서 만들수 있는 경우의수
for i in range(1, n + 1):
    f[i] = f[i - 1] * i     # 팩토리얼 공식

# 문제 종류 및 순열 데이터
array = list(map(int, input().split()))

if array[0] == 1:   # 순열을 출력하는 문제
    k = array[1]
    for i in range(1, n + 1):
        cnt = 1     # 해당 자리애서 남은 수 중 몇 번째 숫자를 사용해야 할지를 정하는 변수
        for j in range(1, n + 1):
            if visited[j]:  # 이미 사용한 숫자는 사용 X
                continue
            if k <= cnt * f[n - i]: # 주어진 k에 따라 각 자리에 들어갈 수 있는 수 찾기
                k -= f[n - i] * (cnt - 1)   #  현재 순서 -= 해당 자리 순열 수 * (cnt - 1)
                s[i] = j    # 현재 자리(S[i])에 j값 저장
                visited[j] = True   # 숫자 j를 사용 숫자로 체크
                break
            cnt += 1
    for i in range(1, n + 1):
        print(s[i], end=' ')
else:   # 순열의 순서를 출력하는 문제
    k = 1   # 순열의 순서 저장 변수
    for i in range(1, n + 1):
        cnt = 0     # 미사용 숫자 세는 변수
        for j in range(1, array[i]):
            if not visited[j]:  # 사용한 숫자가 아니라면
                cnt += 1    # 미사용 숫자 개수 만큼 카운트
        k += cnt * f[n - i] # 자릿수에 따라 순서 더하기
        visited[array[i]] = True
    print(k)