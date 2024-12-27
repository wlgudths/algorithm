def count_sort(arr):
    count = [0] * 31
    sorted_array = []

    for i in range(len(arr)):
        count[arr[i]] += 1
    
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_array.append(i)
    
    return sorted_array

def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    level = []
    cut = custom_round(n * 0.15)
    
    for _ in range(n):
        level.append(int(input()))

    level = count_sort(level)
    level = level[cut : n - cut]

    print(custom_round(sum(level) / len(level)))