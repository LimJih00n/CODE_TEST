N = int(input())
ans=[]
count=0
while N:
    N-=1
    arr = list(map(int,input().split()))
    if sum(arr)/len(arr) >= 60:
        ans.append("pass")
        count+=1
    else:
        ans.append("fail")
ans.append(str(count))
print("\n".join(ans))
