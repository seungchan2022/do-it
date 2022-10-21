n = int(input())
a = list(map(int, input().split()))
stack = []      # 스택
result = [-1] * n     # 결과 리스트

for i in range(n):
    # 스택이 비어있지 않고 현재 수열이 스택 top인덱스가 가리키는 수열보다 클 경우
    while stack and a[stack[-1]] < a[i]:
        result[stack.pop()] = a[i]
    stack.append(i)     # 스택에 인덱스 형태로 표현

"""
while stack:    # 수열의 길이만큼 반복문을 돌고, 스택이 비어있지 않다면 스택이 빌 때까지 
    result[stack.pop()] = -1

이러면 result = [0] * n로 설정
"""

for i in range(n):
    print(result[i], end=' ')