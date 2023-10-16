# 백준 1543 : 문서검색

'''
아이디어
1. replace
'''

# 입력
words = input()
word = input()

change = words.replace(word, '*')

# 출력
print(change.count('*'))
