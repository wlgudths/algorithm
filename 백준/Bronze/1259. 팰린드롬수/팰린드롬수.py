while True:
    num = input()
    if num == '0':
        break
    
    mid = len(num) // 2
    
    if len(num) % 2 == 0:
        left = num[:mid]
        right = num[-1:mid-1:-1]

        if left == right:
            print('yes')
        else:
            print('no')
    
    else:
        left = num[:mid]
        right = num[-1:mid:-1]

        if left == right:
            print('yes')
        else:
            print('no')