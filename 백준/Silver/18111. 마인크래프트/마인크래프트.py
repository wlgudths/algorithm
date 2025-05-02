import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

min_h = min(min(row) for row in land)
max_h = max(max(row) for row in land)
ans = (float('inf'), -1)

for target in range(min_h, max_h + 1):
    time = 0
    blocks = b

    for i in range(n):
        for j in range(m):
            h = land[i][j]

            if h > target:
                time += 2 * (h - target)
                blocks += (h - target)
            
            else:
                time += (target - h)
                blocks -= (target - h)
    
    if blocks >= 0:
        if time < ans[0] or (time == ans[0] and target > ans[1]):
            ans = (time, target)

print(ans[0], ans[1])