# 백준 2309 : 일곱난쟁이

from itertools import combinations

# 입력
dwarf = [int(input()) for _ in range(9)]

# 의심 난쟁이 두 명씩 뽑기
fake_lst = list(combinations(dwarf,2))

# 가짜 난쟁이 키의 합
fake_num = sum(dwarf) - 100

# 가짜 난쟁이 찾아내기
for i in fake_lst:
    if sum(i) == fake_num:
        fake = i
        break

# 오름차순 정렬
dwarf.sort()

# 가짜 난쟁이를 제외한 진짜 난쟁이들 출력
for i in dwarf:
    if i not in fake:
        print(i)

