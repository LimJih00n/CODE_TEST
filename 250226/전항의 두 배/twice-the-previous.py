n,m = map(int,input().split())
ans = [n,m]
i=2
while True:
    ans.append(ans[i-1]+ans[i-2]*2)
    if i==9:
        break
    i+=1
print(*ans)