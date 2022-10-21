n = int(input())

stack = []      # 스택
answer = []     # 결과 값('+', '-')
count = 1       # 스택에 들어갈 자연수값(1씩 증가시켜 주면서 오름차순으로 push)
result = True

for i in range(n):
    num = int(input())
    while count <= num:     # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(count)
        answer.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:   
        result = False
        break   # top이 num보다 크면 num은 top보다 더 아래에 있기 때문에 수열을 만들수 없다

if result == False:
    print('No')
else:
    for i in answer:
        print(i)