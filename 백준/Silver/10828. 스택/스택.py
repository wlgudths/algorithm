stack = []
command = []

n = int(input())

for _ in range(n):
    command.append(input().split())

for i in command:
    if len(i) == 2: # push
        stack.append(i[1])
    
    elif i[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif i[0] == 'size':
        print(len(stack))
    
    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif i[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    

