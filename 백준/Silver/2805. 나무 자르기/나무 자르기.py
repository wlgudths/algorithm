n, m = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)
ans = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(map(lambda x: x - mid if x > mid else 0, trees))

    if total >= m:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(ans)