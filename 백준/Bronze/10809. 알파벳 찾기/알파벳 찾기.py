s = input()
words = dict()
alpha = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i, a in enumerate(s):
    if a not in words:
        words[a] = i

for i in alpha:
    if i in s:
        result.append(words[i])
    else:
        result.append(-1)

result = map(str, result)
print(' '.join(result))