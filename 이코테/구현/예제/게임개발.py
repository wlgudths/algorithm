# 맵 입력 받기
n, m = map(int, input().split())

# 캐릭터 위치와 방향 입력 받기
x, y, d = map(int, input().split())

# 맵 정보 입력 받기
maps = [list(map(int, input().split())) for _ in range(n)]

# 방문 정보
check = [[0 for _ in range(m)] for _ in range(n)]

# 동서남북 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
   for j in range(m):
        if maps[i][j] == 0:
            # 현재 위치 방문
            check[i][j] = 1
            # 현재 위치에서 동서남북 살펴보기
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx <= n and nx >= 0 and ny <= m and ny >= 0:
                    if maps[nx][ny] != 1 and check[nx][ny] != 1:
                        check[nx][ny] = 1

# 결과 출력
cnt = 0
for i in check:
    cnt += sum(i)

print(cnt)