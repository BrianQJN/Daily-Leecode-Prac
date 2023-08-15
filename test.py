dp = [[0]*8 for _ in range(8)]
dp[0][1] = 1
dp[0][-1] = 1

print(dp[0][-3])