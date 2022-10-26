# 2751

# 병합 정렬

def merge_sort(array):
    if len(array) <= 1:
        return array

    # 재귀함수를 이용해 분할
    mid = len(array) // 2   # 중간점
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0   # k: 정렬하는 배열의 index

    # 양쪽 그룹의 index가 가리키는 값을 비교한 후 더 작은수를 선택해 리스트에 저장하고
    # 선택된 데이터와 정렬하는 배열의 index값을 + 1, 반복문이 끝나고 남아 있는 데이터 처리
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k  += 1

    # 한쪽 그룹이 모두 정렬된 후 남아 있는 요소들 정렬하는 배열(array)에 넣기
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

# 데이터 입력
n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

result = merge_sort(array)

for i in result:
    print(i)



# 병합 정렬 개념 설명
# https://www.youtube.com/watch?v=ctkuGoJPmAE
