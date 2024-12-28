n = int(input())
for _ in range(n):
    score = 0
    temp = 0
    quiz = input()
    for i in quiz:
        if i == 'O':
            temp += 1
        else:
            temp = 0
        
        score += temp
    
    print(score)