n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

cur_dir = 0
dir_move = [(0,-1),(-1,0),(0,1),(1,0)]
visted = set()
cur_p = (n-1,n-1)

def check_b(r,c):
    if r<n and c<n and r>=0 and c>=0:
        return True
    return False

for i in range(n*n,0,-1):
    visted.add(cur_p)
    grid[cur_p[0]][cur_p[1]] = i 
    next_p = (cur_p[0] + dir_move[cur_dir][0],cur_p[1] + dir_move[cur_dir][1])
    if check_b(next_p[0],next_p[1]) and next_p not in visted:
        cur_p= next_p
    else:
        cur_dir = cur_dir + 1 if cur_dir<3 else 0
        next_p = (cur_p[0] + dir_move[cur_dir][0],cur_p[1] + dir_move[cur_dir][1])
        cur_p= next_p
for row in grid:
    print(*row)



