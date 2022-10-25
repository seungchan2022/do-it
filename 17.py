import sys
input = sys.stdin.readline
print = sys.stdout.write    # 하나의 텍스트가 표시된 후 새 줄로 전화되지 않는다.
a = list(input())

for i in range(len(a) -1):
    max = i
    for j in range(i + 1, len(a)):
        if a[j] > a[max]:   # a배열에서 최대값 찾기(내림차순 정렬이므로)
            max = j
    if a[i] < a[max]:
        a[i], a[max] = a[max], a[i]

print(''.join(a))

----------------------------------------------------------
n = list(input())

n.sort(reverse=True)

for i in n:
    print(i, end='')
