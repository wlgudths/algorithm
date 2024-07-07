# 영화감독 숌 <https://www.acmicpc.net/problem/1436>

# 입력
n = int(input())

# 영화 제목
title = 666

# n과 비교할 숫자
cnt = 0

while True:
    # 666이 영화제목에 들어가면 cnt = cnt + 1
    if '666' in str(title):
      cnt += 1
    # n과 cnt가 같으면 while문 탈출
    if n == cnt:
        break
    
    # 영화 제목 + 1
    title += 1

# 출력
print(title)