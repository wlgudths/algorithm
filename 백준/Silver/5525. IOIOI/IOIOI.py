n = int(input())
m = int(input())
s = input()

p = 'IOI' + ('OI' * (n - 1))
length = len(p)
ans = 0

for i in range(0, m - length + 1):
    if s[i : i + length] == p:
        ans += 1

print(ans)