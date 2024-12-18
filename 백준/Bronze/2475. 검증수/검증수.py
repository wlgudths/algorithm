num_list = list(map(int, input().split()))

result = 0

for i in num_list:
    result += (i * i)
print(result % 10)