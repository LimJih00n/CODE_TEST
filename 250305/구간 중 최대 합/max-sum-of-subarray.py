n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = float("-inf")
for i in range(0,n):
    tot = 0
    for j in range(i,i+k):
        if j>=n:
            break
        tot += arr[j]
    ans = max(ans,tot)
print(ans)