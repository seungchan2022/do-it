# 삽입 정렬

n = int(input())
a = list(map(int, input().split()))
s = [0] * n     # 합 배열 저장 리스트

for i in range(1, n):       # 삽입 정렬은 뒤에서 비교하므로 index1이 index0과 비교 되는 것부터 시작한다
    insert_point = i
    insert_value = a[i]
    for j in range(i - 1, -1, -1):      # 뒤에서 부터 비교
        if a[i] > a[j]:     # a[i]: 정렬 할 데이터, a[j]: 비교 할 데이터 들
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    # 데이터를 정렬 하면 비교 해서 밀려난 데이터를 index 다시 설정
    for j in range(i, insert_point, -1):
        a[j] = a[j - 1]
    a[insert_point] = insert_value

s[0] = a[0]

for i in range(1, n):   # 합 배열 만들기
    s[i] = s[i - 1] + a[i]  # 합 배열 공식


result = 0

for i in range(n):
    result += s[i]

print(result)

# 27 ~ 32  --> print(sum(s))


"""
n = int(input())
a = list(map(int, input().split()))
a.sort()

count = 0   
sum = 0

for i in a:
    count += i
    sum += count

print(sum)
"""