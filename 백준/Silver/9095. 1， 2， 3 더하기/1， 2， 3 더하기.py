t = int(input())

dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4

for _ in range(t):
    t = int(input())
    if t <= 3:
        print(dp[t])
    else:
        for i in range(4, t + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    
        print(dp[t])