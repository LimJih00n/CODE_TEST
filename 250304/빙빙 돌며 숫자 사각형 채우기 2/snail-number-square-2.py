n, m = map(int, input().split())

# Please write your code here.

visited = set()

move_dir = [(1,0),(0,1),(-1,0),(0,-1)]
cur_dir = 0
arr = [[0]*m for i in range(n)]
def check_b(r,c):
    if r<n and c<m and r>=0 and c>=0:
        return True
    return False
cur_p=[0,0]
for i in range(1,n*m+1):
    visited.add(tuple(cur_p))
    
    arr[cur_p[0]][cur_p[1]] = i
    next_p = (cur_p[0]+move_dir[cur_dir][0],cur_p[1]+move_dir[cur_dir][1]) 
    if check_b(next_p[0],next_p[1])  and next_p not in visited:
        cur_p = next_p
    else:
        cur_dir = cur_dir +1 if cur_dir <3 else 0
        next_p = (cur_p[0]+move_dir[cur_dir][0],cur_p[1]+move_dir[cur_dir][1]) 
        cur_p = next_p
for row in arr:
    print(*row)

    

