n = int(input())
nums = list(map(int, input().split()))

cnt = 0

for i in nums:
    if i == 1:
        continue
    else:
        temp = 0
        for j in range(2, i + 1):
            if i % j == 0:
                temp += 1
        
        if temp == 1:
            cnt += 1

print(cnt)