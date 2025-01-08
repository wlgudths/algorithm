import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    op = input().strip()
    if op == 'all':
        s = set(range(1, 21))
    elif op == 'empty':
        s = set()
    else:
        command, num = op.split()
        num = int(num)
        
        if command == 'add':
            s.add(num)
        elif command == 'check':
            if num in s:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num) 
        elif command == 'remove':
            s.discard(num)