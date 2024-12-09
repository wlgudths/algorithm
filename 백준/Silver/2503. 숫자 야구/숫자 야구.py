from itertools import permutations

nums = list(permutations(list(range(1, 10)), 3))
for _ in range(int(input())):
    num, s, b = map(int, input().split())
    result = []

    for check in nums:
        cnt_s, cnt_b = 0, 0

        for i, str_num in enumerate(str(num)):
            if int(str_num) == check[i]:
                cnt_s += 1
            if int(str_num) != check[i] and int(str_num) in check:
                cnt_b += 1
        
        if s == cnt_s and b == cnt_b:
            result.append(check)
        nums = result

print(len(result))