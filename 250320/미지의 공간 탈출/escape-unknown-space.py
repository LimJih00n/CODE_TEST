import collections


def move_func(map_idx,next_r,next_c):
    next_map_idx = map_idx
    re_next_r,re_next_c = next_r,next_c
    move_dir = "S"
    # 그냥 안움직이는 경우도 추가해야한다. => 경계가 아닌경우도
     
   
    if map_idx != 0 and map_idx != 1:
        if next_c == M:
            re_next_c = 0
            next_map_idx = map_idx +1 if map_idx<5 else 2 
        elif next_c == -1:
            re_next_c =M-1
            next_map_idx = map_idx -1 if map_idx>2 else 5
        elif next_r<0: # -> 1
            if map_idx == 2:
                
                next_map_idx = 1
                re_next_r,re_next_c  = M-1,next_c
                
            if map_idx == 3:
                next_map_idx = 1
                re_next_r,re_next_c  = M-next_c-1,M-1
            if map_idx == 4:
                next_map_idx = 1
                re_next_r,re_next_c  = 0,M-next_c-1
            if map_idx == 5:
                next_map_idx = 1
                re_next_r,re_next_c  = next_c,0
        
        elif next_r>=M:
            if map_idx == 2:
                next_map_idx = 0
                re_next_r,re_next_c  = M+s3dr , next_c+s3dc
            if map_idx == 3:
                next_map_idx = 0
                re_next_r,re_next_c  = s3dr+M-next_c-1  ,M+s3dc
            if map_idx == 4:
                next_map_idx = 0
                re_next_r,re_next_c  = s3dr-1,s3dc+M-next_c-1
            if map_idx == 5:
                next_map_idx = 0
                re_next_r,re_next_c  = s3dr+next_c,s3dc-1
    
            
    if map_idx == 1:
        if next_r>=M: # 1->2
            
            re_next_r,re_next_c= 0,next_c
            next_map_idx = 2
        elif next_c>=M: #1->3 
            re_next_r,re_next_c = 0,M-next_r-1
            next_map_idx = 3
        elif next_r<0: #1->4
            re_next_r,re_next_c=0,M-next_c-1
            next_map_idx = 4
        elif next_c<0: #1->5
            re_next_r,re_next_c=0,next_r
            next_map_idx = 5
    
    
    return next_map_idx,re_next_r,re_next_c

N,M,F = map(int,input().split())

space_map={
}
map2d = [list(map(int,input().split())) for i in range(N)]
space_map[0] = map2d
map3d_3 = [list(map(int,input().split())) for i in range(M)]
map3d_5 = [list(map(int,input().split())) for i in range(M)]
map3d_2 = [list(map(int,input().split())) for i in range(M)]
map3d_4 = [list(map(int,input().split())) for i in range(M)]
map3d_1 = [list(map(int,input().split())) for i in range(M)]


tiem_error = [list(map(int,input().split())) for i in range(F)]


space_map[1] = map3d_1
space_map[2] = map3d_2
space_map[3] = map3d_3
space_map[4] = map3d_4
space_map[5] = map3d_5

s3dr,s3dc = 0,0

start_dim,start_r,start_c =1,0,0

find_=False
for r in range(N):
    for c in range(N):
        
        if space_map[0][r][c] == 3:
            s3dr,s3dc =r,c
        
            find_ = True
            break
    if find_:
        break


goal_r,goal_c =[(r,c) for r in range(N) for c in range(N) if space_map[0][r][c] == 4][0]

start_r,start_c = [(r,c) for r in range(M) for c in range(M) if space_map[1][r][c] == 2][0]

start_node = (1,start_r,start_c)
goal_node = (0,goal_r,goal_c)


def check_b(r,c,n):
    if r>=0 and c>=0 and r<n and c<n:
        return True
    return False

def bfs(start_node):
    queue= collections.deque()
    visted = set()
    queue.append((start_node,0))
    visted.add(start_node)
    
    move_dir =[
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (0,0)
    ]
    
    while queue:
        cur_node,time_ = queue.popleft()
#        print(cur_node)
        for i in range(len(tiem_error)): # 시간 이상 전이 현상
            error = tiem_error[i]
            if time_==0:
                continue
            if error[3]%time_ == 0:
                r = error[0]
                c = error[1]
                space_map[0][r][c] = 1
                nr,nc = r+move_dir[error[2]][0],c+move_dir[error[2]][1]
                if check_b(nr,nc,N) and space_map[0][nr][nc] != 1 and space_map[0][nr][nc] != 4:
                    error[0],error[1] = nr ,nc 
                else:
                    error[2] = 4
        
        for i in range(4):
            if cur_node[0] != 0:
                cur_dim,nr,nc = cur_node[0],cur_node[1]+move_dir[i][0],cur_node[2]+move_dir[i][1]
                
                next_dim,next_r,next_c = move_func(cur_dim,nr,nc)
                next_node = (next_dim,next_r,next_c)
         #      print((cur_dim,nr,nc),"->",next_node)
                
                if space_map[next_dim][next_r][next_c] != 1 and next_node not in visted:
          #          print("in",next_node)
                    queue.append((next_node,time_+1))
                    visted.add((cur_dim,nr,nc))
            else:
                cur_dim,nr,nc = cur_node[0],cur_node[1]+move_dir[i][0],cur_node[2]+move_dir[i][1]
                next_node = (cur_dim,nr,nc)
                if check_b(nr,nc,N) and space_map[0][nr][nc] != 1 and next_node not in visted:
                    if space_map[0][nr][nc] == 4:
                        return time_+1
                    queue.append((next_node,time_+1))
                    visted.add(next_node)
    return -1
                    
                
        
        
    
'''

def print_all_map():
    
    for i in range(6):
        print("===",i,"===")
        for row in space_map[i]:
            print(* row)
print_all_map()
'''

ans = bfs(start_node)
if ans == -1:
    print(-1)
else:
    print(ans)

'''
print(move_func(2,-1,2)) # 1->4 ok
print(move_func(3,-1,2)) #1->5 ok
print(move_func(4,-1,2))  #1->3 okf
print(move_func(5,-1,2)) #1->2 ok
'''

'''
print(move_func(1,-1,2)) # 1->4 ok
print(move_func(1,2,-1)) #1->5 ok
print(move_func(1,2,3))  #1->3 okf
print(move_func(1,3,2)) #1->2 ok

print(move_func(2,0,3))# 2->3 :0,0
print(move_func(3,0,3))#3->4 :0,0
print(move_func(4,0,3))#4->5 :0,0
print(move_func(5,0,3))#5->2 :0,0


print(move_func(2,0,-1))# 2->5 :0,2
print(move_func(3,0,-1))#3->2: 0,2
print(move_func(4,0,-1))#4->3 :0,2
print(move_func(5,0,-1))#5->4 :0,2
print("=========")
print(move_func(2,3,1))#2->0 : ok
print(move_func(3,3,1))#3->0 x
print(move_func(4,3,1)) #4->0x
print(move_func(5,3,1))#5->0 x (4,1)

#print(move_func(3,2,3)) # ok =>
#print(move_func(2,-1,0)) # 정답: 1,2
#print(move_func(5,2,-1)) # 정답: 4,1
#print(move_func(4,3,0))  # 5,2 ok v
'''

