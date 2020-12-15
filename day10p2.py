n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
d.sort()
mx = d[-1]
dp = [0] * (mx+1)
dp[0] = 1
for i in range(n):
    for base in range(max(0, d[i]-3), d[i]):
        dp[d[i]] += dp[base]
print(dp[mx])