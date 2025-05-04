from collections import defaultdict

n = int(input())
s = list(map(int, input().split()))

counter = defaultdict(int)
left = 0
max_len = 0

for right in range(n):
    counter[s[right]] += 1

    while len(counter) > 2:
        counter[s[left]] -= 1

        if counter[s[left]] == 0:
            del counter[s[left]]
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)