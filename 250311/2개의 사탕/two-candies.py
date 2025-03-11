'''
주의할점
오탈자 주의 i 0,1,3,4 해서 오류 남
min,max 주의하기 
'''
import collections
N,M = map(int,input().split())
arr = [list(input()) for i in range(N)]

start_r_po = (0,0,"R")
start_b_po = (0,0,"B")
start_po = (0,0,0,0) #rr,rc,br,bc
O_po = (0,0)
for r in range(N):
    for c in range(M):
        if arr[r][c] == "R":
            start_r_po = (r,c)
        if arr[r][c] == "B":
            start_b_po = (r,c)
        if arr[r][c] == "O":
            O_po = (r,c)
start_po = (start_r_po[0],start_r_po[1],start_b_po[0],start_b_po[1])

dir_ = 0
move_dir = [
    (-1,0), #U
    (1,0), #D
    (0,1), #R
    (0,-1) #L 
]

def move_candy(sr,sc,cur_dir): #r,c,dir로 닿기전까지 이동하는 함수 
    r,c= sr,sc 
    while True:
        nr = r+move_dir[cur_dir][0]
        nc = c+move_dir[cur_dir][1]
        if (nr,nc) == O_po:
            r,c=nr,nc
            break
        if arr[nr][nc]=="#" or arr[nr][nc]=="R" or arr[nr][nc]=="B":
            break # 벽에 닿으면 종료 
        
        r,c = nr,nc
    return (r,c)
ans = float("inf")


def print_arr(move,i):
    print("=================",move,i)
    for row in arr:
        print(*row)
    print("=================")

def bfs():
    global ans
    queue = collections.deque()
    visted = set()
    move_count = 0
    path = []
    queue.append((start_po,move_count,path))
    visted.add(start_po)
    
    while queue:
        cur_po,cur_move_count,cur_path = queue.popleft()
        cur_move_count += 1



        for i in range(4):
            
            
            first_move = "R"
            if i == 0: # up. r이 작은 거 부터 시작
                first_move = "B" if cur_po[0] > cur_po[2] else "R" # 
            if i == 1:# down r이 큰 거 부터 시작. 
                first_move = "B" if cur_po[0] < cur_po[2] else "R"
            if i==2:
                first_move = "B" if cur_po[1] < cur_po[3] else "R"
            if  i==3:
                first_move = "B" if cur_po[1] > cur_po[3] else "R"

            if first_move == "B": # 먼저 움직이는 거 반영.& 상태 반영.
                next_b_po = move_candy(cur_po[2],cur_po[3],i)
                arr[cur_po[2]][cur_po[3]] = "."
                arr[next_b_po[0]][next_b_po[1]] = "B"

                next_r_po = move_candy(cur_po[0],cur_po[1],i)
                arr[cur_po[0]][cur_po[1]] = "."
                
            else:
                next_r_po = move_candy(cur_po[0],cur_po[1],i)
                arr[cur_po[0]][cur_po[1]] = "."
                arr[next_r_po[0]][next_r_po[1]] = "R"

                next_b_po = move_candy(cur_po[2],cur_po[3],i)
                arr[cur_po[2]][cur_po[3]] = "."
                
            
            
            #print(cur_po,next_r_po,next_b_po,first_move,i)
            arr[next_b_po[0]][next_b_po[1]] = "B"
            arr[next_r_po[0]][next_r_po[1]] = "R"
            #print(cur_path)
            #print_arr(cur_move_count,i)
            arr[next_b_po[0]][next_b_po[1]] = "."
            arr[next_r_po[0]][next_r_po[1]] = "."
            
            if O_po == next_r_po and O_po != next_b_po: #빨간 들어오고 파란은 안들어옴
                ans = min(ans,cur_move_count)
                continue
            if O_po == next_b_po: # 파란색이 들어옴 
                continue

            next_po = (next_r_po[0],next_r_po[1],next_b_po[0],next_b_po[1])
            if next_po not in visted and cur_move_count<10: #10번이내 & 정점 아닐 경우
                visted.add(next_po)
                next_path = cur_path[:]
                next_path.append(i)
                queue.append((next_po,cur_move_count,next_path))
    
    
    ans = ans if ans != float("inf") else -1
    return ans
print(bfs())


