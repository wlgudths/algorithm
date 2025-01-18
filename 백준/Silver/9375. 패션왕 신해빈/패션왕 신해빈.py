t = int(input())
for _ in range(t):
    n = int(input())
    
    clothes = {}
    
    # 옷 정보 입력 및 타입별 개수 저장
    for _ in range(n):
        _, t = input().split()
        if t in clothes:
            clothes[t] += 1
        else:
            clothes[t] = 1
    
    # 조합 계산
    result = 1
    for count in clothes.values():
        result *= (count + 1)  # 각 타입에서 옷을 선택하지 않는 경우 포함

    # 아무것도 입지 않는 경우 제외
    print(result - 1)
