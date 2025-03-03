N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

check_po = [(r,c) for r in range(N) for c in range(N) if arr[r][c]==0 or arr[r][c]==1]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def check_b(r,c):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    return False
ans = 0
for r,c in check_po:
    
    
    count=0
    for sdr,sdc in zip(dr,dc):
        
        
        if check_b(r+sdr,c+sdc):
            if arr[r+sdr][c+sdc] == 1:
                count+=1
    if count>=3:
        ans +=1
    
    
    
    count=0
print(ans)
        

