# 프로그래머스 Lv.01 삼총사

def solution(number):
    # 출력 및 정답
    answer = 0

    # 3중 반복문을 통해 number 원소 3개씩 뽑기
    for i in range(0, len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                # 원소 3개의 합이 0이라면, 즉, 삼총사라면 정답 += 1
                if (number[i] + number[j] + number[k]) == 0:
                    answer += 1
    return answer
