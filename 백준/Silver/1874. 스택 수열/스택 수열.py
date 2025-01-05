n = int(input())
nums = [int(input()) for _ in range(n)]
temp = sorted(nums, reverse=True)
stack = []
comparison = []
result = ''
idx = 0

while idx < n:
    num = nums[idx]
    
    if temp and num >= temp[-1]:
        stack.append(temp.pop())
        result += '+'
    elif num == stack[-1]:
        comparison.append(stack.pop())
        result += '-'
        idx += 1
    else:
        break

if comparison == nums:
    for i in result:
        print(i)
else:
    print('NO')
    