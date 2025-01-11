n, m = map(int, input().split())

# 번호 -> 이름 딕셔너리와 이름 -> 번호 딕셔너리 생성
book_by_index = {}
book_by_name = {}

for i in range(1, n + 1):
    name = input()
    book_by_index[i] = name
    book_by_name[name] = i

for _ in range(m):
    question = input()
    if question.isdigit():
        # 번호로 이름 찾기
        print(book_by_index[int(question)])
    else:
        # 이름으로 번호 찾기
        print(book_by_name[question])
