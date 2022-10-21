import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))

def quicksort(s, e, k):     # s: 시작, e: 종료
    global a
    if s < e:
        pivot = partition(s, e)
        if pivot == k:   # k번째 수가 pivot이면
            return 
        elif pivot > k:  # k가 pivot보다 작으면 왼쪽 그룹만 정렬
            quicksort(s, pivot - 1)
        else:            # k가 pivot보다 크면 오른쪽 그룹만 정렬
            quicksort(pivot + 1, e)

def swap(i, j):
    global a
    a[i], a[j] = a[j], a[i]

def partition(s, e):
    global a
    # 데이터가 2개인 경우는 바로 비교하여 정렬
    if s + 1 == e:
        if a[s] > a[e]:
            swap(s, e)
        return e

    m = (s + e) // 2    # m: 중앙값
    swap(s, m)          # 중앙값을 시작 위치와 swap
    pivot = a[s]        # pivot을 시작 위치 값으로 저장
    i = s + 1           # 시작점
    j = e               # 종료점
    
    while i <= j:
        # 피벗보다 작은 수가 나올 때까지 j 감수
        while pivot < a[j] and j > 0:   
            j -= 1
        # 피벗보다 큰 수가 나올 때까지 i 증가
        while pivot > a[i] and i < len(a) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1
    
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정(피벗 데이터를 나뉜 두 그룹이 경계 index에 저장)
    a[s] = a[j]
    a[j] = pivot
    return j

quicksort(0, n - 1, k - 1)
print(a[k - 1])