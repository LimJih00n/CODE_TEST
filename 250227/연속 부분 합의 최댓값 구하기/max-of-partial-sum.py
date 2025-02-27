n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# dp[i] = max(dp[i-1]+dp[i],dp[i])

dp = [0] * (n)
dp[0] = arr[0]
for i in range(1,len(arr)):
    dp[i] = max(dp[i-1]+arr[i],arr[i])

print(max(dp))
