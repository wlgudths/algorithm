# [프로그래머스] Lv.01 : 같은 숫자는 싫어 (파이썬)

# 나의 풀이
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return(answer)

# 다른 사람 풀이
def diff_solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] != [i]:
            answer.append(i)
    return answer
