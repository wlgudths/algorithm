# 입력 받기
s = 'aukks'
skip = 'wbqd'
index = 5

result = ''

ord_s = list(map(lambda x : ord(x), s))
ord_skip = list(map(lambda x : ord(x), skip))

for i in ord_s:
    cnt = 0
    for j in range(i, i + index + 1):
        if j in ord_skip:
            cnt += 1

    if i + index + cnt > 122:
        result += chr(97 + (i + index + cnt) % 123)
    else:
        result += chr((i + index + cnt))
    

print(result)

