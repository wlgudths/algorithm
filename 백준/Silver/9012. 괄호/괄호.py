for _ in range(int(input())):
    ps = input()
    stack = []

    for s in ps:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
