import sys
input = sys.stdin.readline

n, m = map(int, input().split())
store = dict()

for _ in range(n):
    adress, password = input().rstrip().split()
    store[adress] = password

for _ in range(m):
    site = input().rstrip()
    print(store[site])