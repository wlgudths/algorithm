l = int(input())
letters = input()

r = 31
m = 1234567891

alphabet = 'abcdefghijklmnopqrstuvwxyz'
hash_mapping = {}
ans = 0

for i, j in enumerate(alphabet):
    hash_mapping[j] = i + 1

for i, letter in enumerate(letters):
    ans += hash_mapping[letter] * (r ** i)

print(ans % m)