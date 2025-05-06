import math 

n = list(map(int, input()))
check = [0] * 10

for i in n:
    if i == 6 or i == 9:
        check[6] += 1
    else:
        check[i] += 1

check[6] = math.ceil(check[6] / 2)

print(max(check))