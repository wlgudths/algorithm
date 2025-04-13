n = int(input())
size = map(int, input().split())
t, p = map(int, input().split())

bundle_p, sep_p = divmod(n, p)

cnt = 0

for i in size:
    cnt += i // t
    if i % t > 0:
        cnt += 1

print(cnt)
print(bundle_p, sep_p)