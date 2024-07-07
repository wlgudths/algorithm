# 생성자 함수
def d(n):
    if n < 10: # 한 자리 수일 경우
        return n + n
    else:
        return n + sum(map(int, str(n))) # n과 각 자리수의 합 더하기

self_num = [True] * 10001 # 셀프넘버 리스트

for i in range(1,len(self_num)): # 1 ~ 10000
    if d(i) <= 10000: # 10000보다 작거나 같을 경우
        self_num[d(i)] = False # 생성자일 경우 False 처리 (셀프넘버가 아닐 경우)


for i in range(1,len(self_num)):
    if self_num[i] == True: print(i) # 셀프넘버(True)일 경우 출력