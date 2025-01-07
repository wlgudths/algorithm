n = int(input())
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))

arr = [0] * 20000001
result = []

for i in n_nums:
    arr[i] += 1

for j in m_nums:
    result.append(arr[j])

print(' '.join(map(str, result)))

