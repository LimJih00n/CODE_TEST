arr = list(map(int,input().split()))
ans = []
for n in arr:
    if n == 0:
        break
    if n %2 == 0:
        ans.append(n//2)
    else:
        ans.append(n+3)
print(*ans)