n = int(input())
POS = [list(map(int,input().split())) for i in range(n)]
ans = float('inf')

for i in range(n):
    pos = POS[:]
    if i==n:
        break
    del pos[i]


    res1 = sorted(pos,key = lambda x:x[0],reverse=True)
    res2 =  sorted(pos,key = lambda x:x[1],reverse=True)
    res3 = sorted(pos,key = lambda x:x[0])
    res4 =  sorted(pos,key = lambda x:x[1])
    
    ans = min(ans,abs(res1[0][0]-res3[0][0])*abs(res2[0][1]-res4[0][1]))
print(ans)