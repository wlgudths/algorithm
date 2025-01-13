n, m = map(int, input().split())
store = dict()

for _ in range(n):
    adress, password = input().split()
    store[adress] = password

for _ in range(m):
    site = input()
    print(store[site])