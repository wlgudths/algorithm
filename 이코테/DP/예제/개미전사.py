# 식량창고의 개수 N 입력 받기
n = int(input())
# 식량창고에 저장된 식량의 개수 K 공백을 구분으로 입력받기
k = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100


d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])
