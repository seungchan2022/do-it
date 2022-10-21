n = int(input())
array = list(map(int, input().split()))
count = 0

array.sort()

for k in range(n):
    find = array[k]
    i = 0
    j = n - 1
    while i < j:
        if array[i] + array[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif array[i] + array[j] < find:
            i += 1
        else:
            j -= 1

print(count)

"""
투 포인터 알고리즘

좋은 수 인지만 판단 하면 되므로 성립하는거 하나만 찾으면 된다
그리고 자기 자신을 좋은 수 만들기에 포함하면 안되므로 이점을 예외로 처리 해야 된다
"""