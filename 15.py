n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

for i in range(n - 1):
    # index가 n - i -1 인 이유는 정렬된 데이터는 다시 확인할 필요 X
    for j in range(0, n - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

for i in range(n):
    print(array[i])

"""
4~

array.sort()

for i in array:
    print(i)
"""
