import sys
input = sys.stdin.readline

s, p = map(int, input().split())
data = input()

a, c, g, t = map(int, input().split())
start = data[:p]    # 시작 문자열

dic = {'A':0, 'C':0, 'G':0, 'T':0}
# 11 ~ 16: start문자열이 부분 문자열 성립하는지 확인 하는 것
for i in start:
    dic[i] += 1
count = 0
if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
    count += 1

s_index = 0
e_index = s_index + p

for i in range(s - p):
    # 1칸 오른쪽 으로 이동하면, 기존의 구간에 비해서 1개가 추가되고, 1개는 빠져 나간다
    dic[data[s_index + i]] -= 1
    dic[data[e_index + i]] += 1
    if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
        count += 1

print(count)

# https://dibrary.tistory.com/164
# 23 ~ 24 위 링크 아래 그림 이해
