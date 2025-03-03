n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
visted = set()

dir_map=[(0,1),(1,0),(0,-1),(-1,0)]
def check_b(r,c):
    if r>=0 and c>=0 and r<n and c<m:
        return True
    return False
po = [0,0]
visted.add(tuple(po))
dir_ =0
for i in range(n*m):
    
    arr[po[0]][po[1]] = i+1
    next_po = [po[0]+dir_map[dir_][0],po[1]+dir_map[dir_][1]]
    if tuple(tuple(next_po)) in visted or not check_b(next_po[0],next_po[1]):
        
        dir_ = dir_ +1 if dir_< 3 else 0
        
        next_po = [po[0]+dir_map[dir_][0],po[1]+dir_map[dir_][1]]
        
    visted.add(tuple(next_po))
    po = [next_po[0],next_po[1]]
    
    
for row in arr:
    print(*row)



    
