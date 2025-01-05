def mod(arr):
    s_arr = sorted(set(arr))
    cnts = []
    for i in s_arr:
        cnts.append((arr.count(i), i))

    cnts.sort(key=lambda x : x[0], reverse=True)
    
    if cnts[0][0] == cnts[1][0]:
        return cnts[1][1]
    else:
        return cnts[0][1]

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

# 산술평균
print(round(sum(nums) / len(nums)))
# 중앙값
print(nums[n // 2])
# 최빈값
print(nums[0] if n == 1 else mod(nums))
# 범위
print(abs(nums[-1] - nums[0]))