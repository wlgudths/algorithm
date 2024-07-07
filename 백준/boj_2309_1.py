# 백준 2309 : 일곱난쟁이


# 입력
dwarf = [int(input()) for _ in range(9)]

# 총합 - 100
fake = sum(dwarf) - 100

# 9명의 난쟁이 중 가짜 난쟁이 뽑기
for i in range(len(dwarf)):
    for j in range(i+1, len(dwarf)):
        if (dwarf[i] + dwarf[j]) == fake:
            fake_1, fake_2 = dwarf[i], dwarf[j]
            break


# 오름차순 정렬
dwarf.sort()

# 출력
for i in dwarf:
    if fake_1 != i and fake_2 != i: # 가짜 난쟁이를 제외하고 print
        print(i)
