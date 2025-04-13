n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

cnt = sum(map(lambda i: i // t + (1 if i % t > 0 else 0), size))
bundle_p, sep_p = divmod(n, p)

print(cnt)
print(bundle_p, sep_p)