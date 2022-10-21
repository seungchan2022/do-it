# 계수 정렬(이코테 개념 보기)

import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001     # 정렬 리스트

for i in range(n):
    # 리스트에 현재 수에 해당하는 index의 값 + 1
    count[int(input())] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):   # 개수만큼 출력
            print(i)