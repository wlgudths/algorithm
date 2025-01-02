t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor =  h * 100 if n % h == 0 else (n % h) * 100
    room = n // h if n % h == 0 else (n // h) + 1
    print(floor + room)