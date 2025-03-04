n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
dr = [1,-1,0,0]
dc = [0,0,1,-1]
arr =[[0]*(n+1) for i in range(n+1)]
def check_b(r,c):
    if r<=n and c<=n and r>0 and c>0:
        return True
    return False
ans =[]
for p in points:
    arr[p[0]][p[1]] = 1
    count=0
    for sdr,sdc in zip(dr,dc):
        
        if check_b(p[0]+sdr,p[1]+sdc):
            if arr[p[0]+sdr][p[1]+sdc] == 1:
                count+=1
    count = 1 if count >=3 else 0
    ans.append(count)
for c in ans:
    print(c)


        
