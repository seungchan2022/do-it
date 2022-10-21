# 1920

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

x = int(input())
data = list(map(int, input().split()))

# 데이터를 하나씩 확인 하면서
for i in data:
    # 해당 값이 존재 하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print(1)
    else:
        print(0)