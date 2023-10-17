# 백준 1065 한수

# 1 <= n <= 1000 

# 100의 자리 한수 판별 함수
def hundred (n):
    if n >= 1000: # 천의 자리숫자가 들어올 경우 False 반환
        return False
    
    temp = list(map(int, str(n)))
    a = temp[0] - temp[1]
    b = temp[1] - temp[2]
    
    # 한수일 경우 True 반환 / 아닐 경우 False 반환
    if a == b:
        return True
    else:
        return False



# 입력
n = int(input())

# 출력 / 한수 개수 카운트
cnt = 0


for i in range(1, n+1): # 1 ~ N 까지 반복
    if i < 100: # 100보다 작을 경우
        cnt += 1
    else: # 100보다 큰 경우
        if hundred(i) == True: # 한수 판별이 True 일 경우 카운트
            cnt += 1

print(cnt)