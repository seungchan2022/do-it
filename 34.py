# 1744

n = int(input())

m_list = []     # 음수 리스트
p_list = []     # 양수 리스트
o_list = []     # 1 리스트
result = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        p_list.append(num)
    elif num <= 0:      # 0도 음수 리스트에 넣음
        m_list.append(num)
    else:
        o_list.append(num)

m_list.sort()       # 오름차순 정렬
p_list.sort(reverse=True)   # 내림차순 정렬

# 양수 계산
# 양수의 개수가 홀수라면 제일 작은 값을 정답에 더하기
if len(p_list) % 2 == 1:
    # 내림차순 정렬 했으므로 마지막 원소가 가장 작은 값
    result += p_list[len(p_list) - 1]   # 마지막 원소 index
    for i in range(0, len(p_list) - 1, 2):
        result += p_list[i] * p_list[i + 1]
# 양수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
else:
    for i in range(0, len(p_list) - 1, 2):
        result += p_list[i] * p_list[i + 1]

# 음수 계산(0 포함)
# 음수의 개수가 홀수라면 제일 큰 값을 정답에 더하기
if len(m_list) % 2 == 1:
    result += m_list[len(m_list) - 1]
    for i in range(0, len(m_list) - 1, 2):
        result += m_list[i] * m_list[i + 1]
# 음수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
else:
    for i in range(0, len(m_list) - 1, 2):
        result += m_list[i] * m_list[i + 1]

# 1 처리
result += len(o_list)

print(result)