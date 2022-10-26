# 1517

import sys
input = sys.stdin.readline

def merge_sort(start, end):
    global count
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        
        a = start       # 앞쪽 그룹의 시작 index
        b = mid + 1     # 뒤쪽 그룹의 시작 index
        tmp = []    # 비교하면서 정렬할 용도의 배열
        while a <= mid and b <= end:
            if array[a] <= array[b]:
                tmp.append(array[a])
                a += 1
            else:
                tmp.append(array[b])
                b += 1
                # count += mid - 들어갈 index + 1
                count += mid - a + 1    # swap 했을때 개수 추가

        # 한쪽 배열이 다 정렬 되었을 때
        if a <= mid:
            tmp += array[a:mid + 1]
        if b <= end:
            tmp += array[b:end + 1]

        for i in range(len(tmp)):
            array[start + i] = tmp[i]
            
count = 0
n = int(input())
array = list(map(int, input().split()))
merge_sort(0, n - 1)
print(count)



# https://jsikim1.tistory.com/300 (그림)
# https://gaza-anywhere-coding.tistory.com/105 (내용)
