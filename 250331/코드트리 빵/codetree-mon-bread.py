'''
m명의 사람이 있다. i분에 출발한다. 각자의 베이스 캠프에서 편의점으로
출반시간이 되기전에는 격자 밖에 있다.
목표로 하는 편의점은 다르다. nxn 크기의 격자에서 움직인다.

사람의 움직임. 1,2,3 순서로 진행. 1분동안 진행
1. 가고 싶은 편의점 향해 "한칸" 움직인다. 최단거리로
상좌우하의 우선순쉬
최단거라 - 칸수가 최소 => bfs 탐색

2. 만약 편의점에 도착시 해당 편의점에서 멈춤 다른 사람은 지나갈 수 없음
but 격자에 있는 사람들이 모두 이동한 후 해당칸을 지나갈 수 없음
=> 다음턴 부터

3. 현재 시간이 t분이고 t<=m 이면
t번 사람은 자신이 가고 싶은 곳과 가장 가까이 있는
베이스 캠프에 들어간다.
여러개인 경우에는 행이 가장 작은 같다면 열이 가장 작은 캠프
이동하는데 시간이 소요되지 않는다
=> 순간이동 시킨다. 

이때부터 다른 사람들은 해당 베이스 캠프가 있는 칸을
지나갈 수 없음. 
- 사람이 움직이더라도 못지나감
- 모두 이동한 후에 지나갈 수 없음 => 턴 이후

동일한칸에 둘이상 가능함.

구현해야하는 함수
1) (sr,sc)와 (gr,gc) 의 최단 경로를 위한 다음 칸을 구하는 함수. => 경로는 의미가 없다 이유: 나중에 막힐 수 있기 때문에 
2) basecamp와 편의점 거리를 세는 함수. => 가장 가까운 거 확인해야함

사람이 아직 이동하지 않은 경우 -> 베이스 캠프에 먼저 두고 그다음에 이동을 시키는 것이다. 

생각해야하는 것: 이동 불가능한 칸을 어떻게 관리할 것인가. 
idea1: 벽 list 만들고 넣어두기. turn 지날때 update
캐릭터의 움직임을 어떻게 관리할 것인가 => 현재 이동중인 캐릭터 pos를 들고 있기. 각 pos를 돌아다니며 탐색하기. 

전체적인 로직

캐릭터 pos 를 돌면서
캐릭터와 goal의 최단 경로중 한칸을 계산한다. 한칸을 이동시킨다.
편의점 도착시 그칸을 못가는 칸에 집어넣는다. 
아직 안들어간 캐릭터를 베이스캠프로 이동시킨다. <- 가장 가까운 베이스 캠프 찾는 함수. 이후 못가는 칸에 집어넣는다. 

편의점 도착할경우 => 현재 탐색하고 있는 사람의 목록에서 재외시킨다. 


최단경로 찾기 함수
bfs사용
간칸은 못감. 벽칸은 못감. 루트 찾았을때. 그 루트의 시작점 칸 반환하기.

캐릭터 위치를 어떻게 관리할지. => 리스트 캐릭터 위치 순회. 찾고 위치이동. 편의점이면 빼기

베이스 캠프 이동 => 갈려는 편의점과 베이스 캠프 목록 탐색 => 가장 가까운 곳으로 이동. 이동 후 배이스캠프에서 제거

바깥에 있다는 것을 어떻게 인지?

틀림 => 시간초과 나옴=> 이유: 매번 bfs를 돌렸기 때문에.. 

방법1. 초기 path를 정해둔다. 만약 가는길이 막힌다면 path를 수정한다. 

'''
import collections 


def game_logic(man_pos,goal_conv_pos,allive_pos,base_camps,wall_pos):
    t=0
    man_move_paths = [[] for i in range(M)]
    is_make_wall = False
    
    while True:
        next_wall_pos = wall_pos[:]
        
        if is_make_wall:
            for i in range(len(man_pos)):
                if man_pos[i] in allive_pos:
                    continue
                if man_pos[i] == (-1,-1):
                    continue
                move_path,dist = find_min_path_point(man_pos[i],goal_conv_pos[i],wall_pos)
                
                man_move_paths[i] = move_path
        
        is_make_wall = False
        
        for i in range(len(man_pos)):
            if man_pos[i] in allive_pos:
                continue
            if man_pos[i] == (-1,-1):
                continue
            
            
            
            man_pos[i] = man_move_paths[i][0]
            
            
            
            if man_pos[i] == goal_conv_pos[i]:
                allive_pos.append(goal_conv_pos[i])
                next_wall_pos.append(goal_conv_pos[i])    
                is_make_wall = True
            
            del man_move_paths[i][0]
            
        if t<M:
            
            base_point = find_near_camp(base_camps,goal_conv_pos[t],wall_pos)
            man_pos[t] = base_point
            next_wall_pos.append(base_point)
            is_make_wall = True
        
        wall_pos = next_wall_pos[:]    
        
        
        #print("=============",t,"==============================")
        #print_cur_state(man_pos,goal_conv_pos,allive_pos,base_camps,wall_pos)
        if len(allive_pos) == len(goal_conv_pos): # 모두 도착함 
            return t 
        t+=1
        
            

def find_near_camp(base_camps,goal_po,wall_pos):
    
    min_dist = N*N
    my_base = (N-1,N-1)
    for camp in base_camps:
        po,dist = find_min_path_point(camp,goal_po,wall_pos)
        if min_dist>dist:
            min_dist = dist 
            my_base = camp 
        if min_dist == dist:
            if camp[0] < my_base[0]:
                my_base = camp
            elif camp[0] == my_base[0]:
                if camp[1]<my_base[1]:
                    my_base = camp
    
    base_camps.remove(my_base)
    return my_base


def check_b(r,c):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    return False 

def find_min_path_point(po,goal_po,wall_pos): # 가장 가까운 칸과 남은 거리를 반환한다. 편의점을 도착한 경우는 한칸이고 길이가 1이다.
    #po와 goal po간의 거리와 최단 경로를 위한 다음칸을 반환한다.
    queue = collections.deque()
    visted = set() 
    visted.add(po)
    path_=[]
    queue.append((po,path_))
    
    move_dir = [
        (-1,0),
        (0,-1),
        (0,1),
        (1,0)
    ]
    
    while queue:
        cur_node,path_ = queue.popleft()
        for move in move_dir:
            nr,nc = cur_node[0]+move[0],cur_node[1]+move[1]
            
            if (nr,nc) not in wall_pos and check_b(nr,nc) and (nr,nc) not in visted:
                visted.add((nr,nc))
                path_.append((nr,nc))
                queue.append(((nr,nc),path_[:]))
                if (nr,nc) == goal_po:
                    return path_,len(path_)
                path_.pop()
    return [po],0 


def print_arr(arr):
    print("="*N)
    for row in arr:
        print(*row)

def print_cur_state(man_pos,goal_conv_pos,allive_pos,base_camps,wall_pos):
    print("cur_all",allive_pos)
    p_arr = [[0]*N for i in range(N)]
    for camp in base_camps:
        p_arr[camp[0]][camp[1]] = 1
    for conv in goal_conv_pos:
        p_arr[conv[0]][conv[1]] = 2
    for po in man_pos:
        if po[0]==-1:
            continue
        p_arr[po[0]][po[1]] = 3
    for po in wall_pos:
        p_arr[po[0]][po[1]] = 4
    print("cur_man",man_pos)
    print_arr(p_arr)
    

wall_pos=[]
base_camps = []
man_pos = []
N = 5
M = 5
goal_conv_pos = []
allive_pos = [] # 도착한 편의점 넣어두기

# 입력이 1,1로 부터 시작함 => 나는 0,0 시작으로 맞추기
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
goal_conv_pos = [list(map(int,input().split())) for i in range(M)]
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            base_camps.append((r,c))

for i in range(M):
    goal_conv_pos[i][0]-=1
    goal_conv_pos[i][1]-=1
    goal_conv_pos[i] = tuple(goal_conv_pos[i])
    man_pos.append((-1,-1))


print(game_logic(man_pos,goal_conv_pos,allive_pos,base_camps,wall_pos)+1)