n = int(input())
array = list(map(int, input().split()))
m = max(array)

data = 0    # 바뀐 시험 점수들의 총합
for i in array:
  data += i / m * 100

result = data / n

print(result)

"""
5 ~ 11
sum = sum(array)
print(sum / m * 100 / 3)

점수가 a, b, c 인경우
((a / m * 100) + (b / m * 100) + (c / m + 100)) / 3 = (a + b + c) / m * 100 / 3
따라서 일일이 변환 점수를 구할 필요 없이 한번에 변환한 점수의 평균 점수를 구할수 있다.
"""