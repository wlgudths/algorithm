# 백준 2798 : 블랙잭

'''
아이디어 1

1. N장의 카드 중 3장의 카드를 뽑는다.
2. 3장의 카드의 합 중 M 보다 큰 카드들을 버린다.
3. 남은 카드 중 카드의 합이 가장 큰 숫자가 정답
'''

# 입력 
n,m = map(int, input().split())
cards = list(map(int, input().split()))

# 카드의 합 담을 리스트
basket = []

# 중복 없이 3장의 카드 뽑기
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            nums = cards[i] + cards[j] + cards[k]
            if nums <= m:
                basket.append(nums)

# 출력
print(max(basket)) # basket 리스트 원소 중 가장 큰 값 출력
                