n = int(input())
ans = [1,n]
i=2
while True:
    ans.append(ans[i-1]+ans[i-2])
    if ans[-1]>100:
        break
    i+=1
print(*ans)