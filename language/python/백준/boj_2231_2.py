# 백준 2231 : 분해합


# 두 번쨰 시도

# 입력
n = int(input()) 

# 결과를 담을 변수
ans = 0

for i in range(1, n+1): # 1 ~ n 까지
    num = i + sum(map(int, str(i))) # i의 분해합

    if num == n: # 생성자의 분해합과 N이 같을 경우
        ans = i # 결과에 생성자 i를 담고 반복문 종료!
        break

# for문을 1부터 n까지 돌며 생성자를 찾게되면 가장 작은 생성자를 찾게 된다.
# 만약 n까지 돌고 나서 생성자가 없을 경우 결과는 그래로 0을 출력하게 된다.


# 결과 출력
print(ans)