# 백준 : 1057 토너먼트

# https://www.acmicpc.net/problem/1057


# 입력
n, kim, lim = map(int, input().split())

# 출력값
round = 0

# 인덱스
kim -= 1
lim -= 1


if n < 2: # 서로 대결하지 않을 경우
    print(-1)
else:
    while n != 1:
        round += 1

        table = [0] * n # 대진표 생성

        table[kim], table[lim] = 1,1 # 김, 임 대진 자리 표시

        # 출력 (김지민과 임한수가 만났을 경우 break)
        for i in range(0, n, 2):
            if sum(table[i : i + 2]) == 2:
                print(round)
                break
    
        # n이 홀수 일 경우
        if n % 2 == 1: n = n // 2 + 1
        else: n //= 2

        kim //= 2
        lim //= 2
        



