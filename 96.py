# 14003
# 이해 X

import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

index = 0
maxLength = 1   # 가장 긴 증가하는 부분 수열 길이 저장
# 현재 가장 유리한 증가 수열 저장 리스트 (처음 B[1]은 A[1]으로 초기화)
B = [0] * 1000001   
# 0 ~ i까지 i를 포함하는 최장 증가 수열의 길이 저장 리스트(처음 D[1]은 1로 초기화)
D = [0] * 1000001   
ans = [0] * 1000001 # 정답 수열 저장 리스트
B[maxLength] = A[1]
D[1] = 1

# 바이너리 서치 구현
def binarysearch(l, r, now):    # 현재 수열이 들어갈 수 있는 위치를 빠르게 찾기 위한 함수
    while l < r:
        mid = (l + r) // 2
        if B[mid] < now:
            l = mid + 1
        else:
            r = mid
    return l

for i in range(2, N + 1):
    if B[maxLength] < A[i]:  # 가장 마지막 수열보다 현재 수열이 큰 경우
        maxLength += 1
        B[maxLength] = A[i] # B 리스트의 끝에 A[i]값 추가
        D[i] = maxLength
    else:  # 바이너리 서치를 이용해 현재 수열이 들어갈 index 찾기
        index = binarysearch(1, maxLength, A[i])
        B[index] = A[i]     # 현재 수열의 값 저장
        D[i] = index

print(maxLength)

index = maxLength
x = B[maxLength] + 1
for i in range(N, 0, -1):
    if D[i] == index and A[i] < x:
        ans[index] = A[i]
        x = A[i]
        index -= 1

for i in range(1, maxLength + 1):
    print(ans[i], end=' ')
    

    
# https://ggam-nyang.tistory.com/40
# https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
