import sys
input = sys.stdin.readline

MAX = 1000000
count = [0] * (MAX + 1)

n = int(input())
for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(MAX + 1):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)