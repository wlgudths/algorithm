# 현재 위치 입력 받기
place = input()

# place 숫자 변환
alpha_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}

# x와 y에 숫자 할당하기
x = alpha_dict[place[0]]
y = int(place[1])

# 총 경우의 수를 담을 변수
cnt = 0

# L자로 움직이는 8가지 경우의 수 정의
moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

for move in moves:
    dx = x + move[0]
    dy = y + move[1]
    
    if dx <= 8 and dx >= 1 and dy <= 8 and dy >= 1:
        cnt += 1

# 결과(경우의 수) 출력
print(cnt)