import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

s = [0]     # 합 배열 리스트(초기값 = 0)
count = 0   # 합 배열에 들어갈 원소 변수

for i in array:
    count += i
    s.append(count)     # 합 배열 만들기

for j in range(m):
    
    a, b = map(int, input().split())
    print(s[b] - s[a - 1])  # 합 배열에서 구간 합 구하기