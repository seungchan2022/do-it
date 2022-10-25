import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    # 정렬 기준을 고려하여 (데이터, index)형태로 저장
    array.append((int(input()), i))

result = 0
array.sort()

for i in range(n):
    # 정렬 전 index - 정렬 후 index 계산의 최대값 저장 
    rsult = max(rseult, array[i][1] - i)

print(max + 1)

"""
버블 정렬의 swap이 한 번도 일어나지 않은 루프가 언제 인지 알아내는 문제
안쪽 루프는 1 ~ n - j까지, 즉 왼쪽에서 오른쪽으로 이동하면서 swap수행
이는 특정 데이터가 안쪽 루프에서 swap의 왼쪽으로 이동할 수 있는 최대 거리가 1이라는 뜻
즉, 데이터 정렬 전 index와 정렬 후 index를 비교해 왼쪽으로 가장 많이 이동한 값을 찾으면 된다.

1. sort()함수를 이용해 배열 정렬
2. 각 데이터마다 정렬 전 index 값에서 정렬 후 index 값을 빼고 최대값을 찾는다. 그리고 swap이 일어나지 않는 반복문이 한 번 더 실행되는 것을 감안해 최대값에 + 1을 한다.
"""
