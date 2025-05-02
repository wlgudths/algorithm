import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
ans = (float('inf'), -1)

flat_land = sum(land, [])
height_counter = Counter(flat_land)

min_h = min(height_counter)
max_h = max(height_counter)

for target in range(min_h, max_h + 1):
    time = 0
    blocks = b

    for h, count in height_counter.items():
        diff = h - target
        if diff > 0:
            time += 2 * diff * count
            blocks += diff * count
        elif diff < 0:
            time += -diff * count
            blocks -= -diff * count

    if blocks >= 0:
        if time < ans[0] or (time == ans[0] and target > ans[1]):
            ans = (time, target)

print(ans[0], ans[1])
