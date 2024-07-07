# 백준 2231 : 분해합

# 첫 시도


# 입력
n = int(input())

# 생성자를 받을 리스트
ans_lst = []

# 정답 비교용
num = n

while n: # n이 0이 될 때까지 반복

    lst = [n] # 각 자리수의 합을 위한 리스트

    for i in str(n): # 각 자리 수 반복 
        lst.append(int(i)) # 리스트에 각 자리수 담기

    if sum(lst) == num: # 각 자리수의 합이 생성자일 경우 
        ans_lst.append(n) # 결과값(생성자)을 담을 리스트에 담기
    
    n -= 1 # n에서 1씩 줄여가며 반복


if len(ans_lst) > 0: # 결과 리스트에 원소가 있을 경우 가장 작은 생성자 출력
    print(min(ans_lst))

else: # 원소가 들어있지않으면 0을 출력
    print(0)




