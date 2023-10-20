# 입력
n = int(input())

# (몸무게, 덩체) 튜플 형식을 입력 받기
lst = [tuple(map(int, input().split())) for _ in range(n)] 

# print(lst) - [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]

for i in lst:
    rank = 1 # 순위 초기화
    w,h = i # 순위를 매길 몸무게와 키;
    for j in lst:
        w1, h1 = j # 비교할 몸무게와 키

        # 비교할 몸무게와 키가 모두 크다면, 즉 순위를 매길 몸무게가 더 작다면 순위 증가
        if w < w1 and h < h1: 
            rank += 1

    print(rank, end=' ') # 순위 이어서 출력하기