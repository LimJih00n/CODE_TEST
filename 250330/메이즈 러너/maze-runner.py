'''
M명의 참가자 미로탈출 게임
NxN r,c (1,1) 시작
미로의 상태
빈칸
벽 (1~9) => 회전시 내굳 -1 0되면 0
출구

1초마다 참가자는 한칸씩 움직인다. 
움직이는 조건
최단거리: 멘하튼
동시에 움직인다. 
상하좌우 & 벽이 없는 곳
출구까지 최단거리가 가까워야함
움직일수있느칸 2개이상 상하 우선
움직일 수 없으면 안움직임
한칸에 2명이상 있을 수 있음

이동끝
미로회전
한명이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다 
2개이상이면 좌상단을 우선으로 둠 => 출구 기준으로 잡으면 안됨. 

선택된 정사각형은 90도 회전하며 히전한 벽은 내구도가 1 깎임

만들어야하는 함수
1) 최단 거리 구하기 -> 이동좌표구하기. (현재좌표 & 출구 받아서 다음좌표 구하기.)
2) 정사각형 잡기 => 한명이상 & 출구포함하는
3) 90도 회전하기 구현하기 (r,c,n) 기준으로 90도 회전하는 함수 만들기. 회전할때 내구도 -1
4) 캐릭터 이동함수

한칸에 2명이상 있을 수 있음 => 캐릭터의 좌표를 리스트로 표현한다
미로의 구조는 2d arr 로 표현한다. 

로직
1) 거리구하기 -> 이동좌표구하기 -> 이동가능한지 안한지 확인해야함. 가능하면 최종거리 +1
2) 이동시키기
3) 미로회전하기 
    -> 제일 작은 정사각형 좌표 잡기 * w 잡기 => 제일 어려울 듯 => ok
    -> 회전시키기 -> 내구도 깎기 => ok
    

만약 r,c를 탐색하면서 n이 2인 크기 부터 시작해서 N까지 반복하기. 찾는 순간 종료    

    
구해야하는 것
이동 거리의 합 & 최종 출구의 위치. 

1,1이 아니라 0,0 을 기준으로 하자.
'''
import copy

N = 5
def find_min_square(man_pos,goal_po):

    
    #좌표를 담고 있으니까 그냥 범위안에 좌표가 있는지 확인하면 빠르다.
    
    for n in range(2,N):
        
        for r in range(N):
            
            
            if r+n>N:
                break
            
            for c in range(N):
                is_e,is_m=False,False
                if c+n>N:
                    break
                
                for po in man_pos:
                    if r<=po[0]<r+n and c<=po[1]<c+n:
                        is_e = True
                    if r<=goal_po[0]<r+n and c<=goal_po[1]<c+n:
                        is_m=True
                if is_e and is_m:
                    return (r,c,n)

def turn_90(arr,R,C,N,man_pos,goal_po):
    #r,c를 기준으로 90도 회전. 
    # col1 col2 col3 => row1 row2 row3 이되며 역순으로
    
    '''
    
    '''

    
    '''
    회전은 조금 더 파파박 짤 수 있게 연습하기.
    
    r,c 기준으로 
    col배열을 만들고
    col들을 저장한다. col배열의 row가 arr의 col이 되게
    그리고 그 col을 역순으로 바꾼다.
    그리고 해당 부분에 그대로 삽입한다. 
    
    r,c -> nr,nc
    nr = c
    nc = N-r-1
    
    (0,0) -> (0,2)
    (0,1) -> (1,2)
    (0,2) -> (2,2)
    
    (1,0) -> (0,1)
    (1,1) -> (1,1)
    (1,2) -> (2,1) 
    
    r  c
    (2,0) -> (0,0)
    (2,1) -> (1,0)
    (2,2) -> (2,0)
    
    
    123
    456
    789
    
    741
    852
    963
    
    r,c -> c,r
    
    따라서 
    1 해당 row뽑기. 
    2역순으로 만들기. 
    3 새로 삽입하기.
    
    man도 같이 회전한다... 이러면 좌표를 찾아서 던져 주는 거 더 나을 듯. 좌표가 어떻게 바뀌는지.. 
    '''
    new_arr = [[0]*N for i in range(N)]
    
    
    for r in range(N):
        for c in range(N):
            new_arr[c][N-r-1] = arr[r+R][c+C]
            
    
    
    
    for r in range(N):
        for c in range(N):
            if new_arr[r][c]=="x":
                goal_po = (r+R,c+C)
                continue
            arr[r+R][c+C] = new_arr[r][c]-1 if new_arr[r][c]>0 else 0
    
    
    #범위안에 있는 경우만 회전해야한다. 
    
    new_man_pos = []
    for po in man_pos:
        if R<=po[0]<R+N and C<=po[1]<C+N:
            cur_r = po[0]-R 
            cur_c = po[1]-C  
            nr = cur_c 
            nc = N-1-cur_r
            new_man_pos.append((nr+R,nc+C))# po[0] , po[1]
            
        else:
            new_man_pos.append(po)
    return arr, goal_po,new_man_pos
    

                
                
def print_arr(arr):
    print("="*len(arr))
    for row in arr:
        print(*row)
                    
def make_arr(arr,goal_po):
    arr[goal_po[0]][goal_po[1]]="x"

def take_min_dist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)

def man_move(r,c,gr,gc):
    move_dir =[
        (-1,0),
        (1,0),
        (0,-1),
        (0,1),
    ]
    nr,nc = r,c
    cur_dist = take_min_dist(r,c,gr,gc)
    for i in range(4):
        if cur_dist > take_min_dist(r+move_dir[i][0],c+move_dir[i][1],gr,gc) and (arr[r+move_dir[i][0]][c+move_dir[i][1]]==0 or arr[r+move_dir[i][0]][c+move_dir[i][1]]=="x"):
            nr,nc = r+move_dir[i][0],c+move_dir[i][1]
            cur_dist = take_min_dist(r+move_dir[i][0],c+move_dir[i][1],gr,gc)
    return (nr,nc)


def print_now_state(man_pos,goal_po,arr):
    p_arr = copy.deepcopy(arr)
    for po in man_pos:
        p_arr[po[0]][po[1]] = "m"
    p_arr[goal_po[0]][goal_po[1]] ="x"
     
    print_arr(p_arr)

def find_goal_roc(arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "x":
                return (r,c)


'''
move_dist = 0
arr = [[0]*5 for i in range(5)]
goal_po = (3,3) #map에도 x로 표시해두기. 
man_pos = [(0,2),(1,0),(2,2)]
print(find_min_square(man_pos,goal_po))
new_man_pos = []
print_now_state(man_pos,goal_po,arr) 
for po in man_pos:
    new_po = man_move(po[0],po[1],goal_po[0],goal_po[1])
    if new_po != po:
        move_dist+=1
    if new_po != goal_po:
        new_man_pos.append(new_po)
print_now_state(new_man_pos,goal_po,arr)
fr,fc,fn=find_min_square(new_man_pos,goal_po)
print(fr,fc,fn)
make_arr(arr,goal_po)
arr,goal_po,new_man_pos=turn_90(arr,fr,fc,fn,new_man_pos,goal_po)
make_arr(arr,goal_po)
man_pos = new_man_pos
print_now_state(man_pos,goal_po,arr)
arr,goal_po,new_man_pos=turn_90(arr,fr,fc,fn,new_man_pos,goal_po)
make_arr(arr,goal_po)
man_pos = new_man_pos
print_now_state(man_pos,goal_po,arr)
'''

#"x"가 실제로 들어가지 않는 오류 고치기.. 나머지는 돌리면 될 듯
# 좌표변환 => 상대좌표로 변환 =>(r,c)빼서 => 변환식 적용 => 다시 대입 => 연습 더하기





def game_logic(arr,man_pos,K):
    t=0
    goal_po = find_goal_roc(arr)
    move_dist = 0
    
    while t<K and len(man_pos)!=0:
        goal_po = find_goal_roc(arr)
        new_man_pos = []
        
        for po in man_pos:
            new_po = man_move(po[0],po[1],goal_po[0],goal_po[1])
            if new_po != po:
                move_dist+=1
            if new_po != goal_po:
                new_man_pos.append(new_po)
        
        #print("cur_dis",move_dist)
        fr,fc,fn=find_min_square(new_man_pos,goal_po)
        #print("sq",fr,fc,fn)
        make_arr(arr,goal_po)
        arr,goal_po,new_man_pos=turn_90(arr,fr,fc,fn,new_man_pos,goal_po)
        make_arr(arr,goal_po)
        man_pos = new_man_pos
        #print_now_state(man_pos,goal_po,arr)
        t+=1
    
    return move_dist,goal_po

NN,MM,KK = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(NN)]
man_pos = [list(map(int,input().split())) for i in range(MM)]
man_pos = [(po[0]-1,po[1]-1) for po in man_pos]
goal_po = list(map(int,input().split()))
arr[goal_po[0]-1][goal_po[1]-1]="x"
#print_arr(arr)
dist,pos = game_logic(arr,man_pos,KK)
print(dist)
print(pos[0]+1,pos[1]+1)

#print(game_logic(arr,man_pos,8))
