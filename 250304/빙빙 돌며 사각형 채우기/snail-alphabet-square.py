n, m = map(int, input().split())

# Please write your code here.
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
"Q","R","S","T","U","V","W","X","Y","Z"]
move_dir = [(0,1),(1,0),(0,-1),(-1,0)]
visted = set()
cur_p = (0,0)
arr =[[0]*m for i in range(n)]
idx = 0
cur_dir = 0
def check_b(r,c):
    if r<n and c<m and r>=0 and c>=0:
        return True
    return False
for i in range(n*m):
    
    arr[cur_p[0]][cur_p[1]] = alpha[idx]
    visted.add(cur_p)
    idx = idx +1 if idx<25 else 0 
    next_p = (cur_p[0]+move_dir[cur_dir][0], cur_p[1]+move_dir[cur_dir][1])
    if check_b(next_p[0],next_p[1]) and next_p not in visted:
        cur_p = next_p
    else:
        cur_dir = cur_dir +1 if cur_dir <3 else 0
        next_p = (cur_p[0]+move_dir[cur_dir][0], cur_p[1]+move_dir[cur_dir][1])
        cur_p = next_p
for row in arr:
    print(*row)