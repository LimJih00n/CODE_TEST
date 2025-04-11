'''
! 피드백
<<python 에서는 [-1] 도 계산이된다. 무언가를 넣을때 항상 범위를 cehck하고 넣기!>>
<<공격을 "한" 전사수이다. 죽은 전사수가 아니다. 그러나 죽은 전사에는 둘다 포함 시켜야한다.>>
=> 먼가 이상할때는 문제와 내 로직을 더 잘 비교하자

-----------------------------------------------------------------------
문제이해
0~N-1 범위로 이루어진 NxN 크기, 메두가
도로0 도로x1
집->공원. 이동. 최단경로로 도로를 따라서 이동한다.
도로위에 있고 공원의 좌표는 다르다

M명의 전사가 마을에 도착. r,c에 위치한다. 최단경로로 이동한다
도로와 비도로를 구분하고 이동한다.

메두사는 전사를 바라봄으로 돌로 만들고 움직임을 멈춘다.

매 턴마다
1. 메두사의 이동 -> 최단경로에 따름. 이동한 칸에 전사가 있다면
전사는 사라진다. -> 상하좌우 우선순위따른다. 경로 없을 수도있다.

2. 메두사 시선
상하좌우 중 하나를 선택해 바라본다.
바라보는 방향은 90도의 시야각을 가진다.
=> 시야각 계산해야한다.
전사에 의해 가려지는 경우가 있다.
=>가려지는 갓도 계산해야한다.

시야안에 있는 적은 돌로변해 움직일 수 없다. 그 턴간. 깉은칸에 2명이상 있다면
그 전사 모두 돌로 변한다.
상하좌우 중 가장 전사를 많이 볼 수 있는 방향. 여러개라면 상하좌우 순

3.전사이동 => 이동 중 같은 칸을 공유할 수 있다.
최대 두칸까지 이동
<이동1>
 1) "거리를 줄일 수 있는" 방향으로 이동한다. 한칸. 상하좌우 우선순위
 2) 격자 밖으로는 나갈 수 없다. 시애에 들어오는 곳으로 이동할 수 없다
<이종2>
 1) "거리를 줄일 수 있는" 방향으로 이동한다. 한칸. 상하좌우 우선순위
 2) 격자 밖으로는 나갈 수 없다. 시애에 들어오는 곳으로 이동할 수 없다

4. 전사의 공격
 메두사와 같은 칸에 도달한 전사는 메두사를 공격한다. 사라진다.

 "거리계산" 맨하튼 거리 기준으로한다.
----------------------------------------
전체 로직
1. 메두사-공원path를 구한다.
2. 메두사는 이동한다. - 전사가 같은 칸이라면 없앤다
3. 메두사 시야를 확인한다. - 가장 높은 곳으로 바라본다
4. 바라본 곳에 있는 전사들을 멈춘다
5. 전사를 이동시킨다.
   -> 거리가 짧아질 수 있는 곳 + 시야에 들어오지 않는 곳
6. 닿는 경우 죽인다.
==> 이동 거리를 구해야한다. 죽는 수를 구해야한다. 돌 수를 구해야한다.
----------------------------------------
구현해야할 내용:
1. 메두사의 시야 구하기. => 8대각선 중 3개를 선택해 양끝으로 쭉 뻗은 다음 가운데 영역을 모두 채운다. => ok
2. 전사로 인해 가려지는 시야 구하기 => 보는 시야각을 받아서 없어지는 좌표를 만든다. => ok
3. TOT 시야구하기 => 전체 시야를 구한다. => ok
4. 돌이 되는 인원 구하기. => 돌이되는 인원을 구한다. => ok
5. 메두사-공원 PATH구하기
6. 움직일 수 있는 인원 구하기 => ok
7. 움직일 수 있는 칸 구하기. => ok

----------------------------------------
메두사 시야 구현하기
(-1,0) 상 =>  (-1,-1)↖  (-1,0)↑ (-1,1) ↗
(0,1) 우 =>    (1,1) ↘   (0,1) →  (-1,1) ↗
(1,0) 하 =>   (1,-1) ↙  (1,0) ↓   (1,1)   ↘
(0,-1) 좌      (1,-1) ↙  (0,-1) ←  (-1,-1)↖

막는 시야 구현하기 + 돌되는 사람 세기.
(-1,0) 상 =>  (-1,-1)↖  (-1,0)↑ (-1,1) ↗
(0,1) 우 =>    (1,1) ↘   (0,1) →  (-1,1) ↗
(1,0) 하 =>   (1,-1) ↙  (1,0) ↓   (1,1)   ↘
(0,-1) 좌      (1,-1) ↙  (0,-1) ←  (-1,-1)↖

1. 시야의 범위안에 전사가 있어야한다.
2. 막는 자기 자신은 다른 사람의 막는 범위에 들어오지 않는다. => 다른 사람의 막는 범위에 들어온다면 의미가 없음
=> 그냥 다 순회하면서 막는 범위를 모두 측정한다.

위를 바라볼때.M_R,M_C
  M_c == w_c (-1,0)↑
  M_c > w_c  (-1,0)↑ (-1,-1)↖
  M_c < w_c  (-1,0)↑ (-1,1) ↗
  --------------------------------
오른쪽을 바라볼때. M_r, M_c
  M_r == w_r  (0,1) →
  M_r > w_c (0,1) →  (-1,1) ↗
  M_r < w_c  (1,1) ↘   (0,1) →
아래를 바라볼때
  M_c == w_c (1,0) ↓
  M_c > w_c  (1,-1) ↙  (1,0) ↓
  M_c < w_c  (1,0) ↓   (1,1)   ↘
왼쪽을 바라볼때
  M_r == w_r  (0,-1) ←
  M_r > w_c   (0,-1) ←  (-1,-1)↖
  M_r < w_c   (1,-1) ↙  (0,-1) ←



각 칸에서 갈 수 있는 끝을 구한다.

그냥 처음부터해서 시야 리스트를 만들고 값들을 넣는다. queue로 맨앞의 값에서 다시 한다. 큐안에 좌표가 있다면 무시한다.
'''
import  collections


def check_B(r,c,N):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    return False

def print_seen_area(arr,N):
    print("===========================")
    p_arr = [[0]*N for i in range(N)]
    for po in arr:
        p_arr[po[0]][po[1]] = 1
    for row in p_arr:
        print(*row)
    print("===========================")


def print_arr(arr):
    print("===========================")
    for row in arr:
        print(*row)
    print("===========================")

def make_first_seen(seen_dir,N,r,c):
    seen_dir_list = [
        [(-1,-1),(-1,0),(-1,1) ], #상
        [(1, -1), (1, 0), (1, 1)],  # 하
        [(1, -1), (0, -1), (-1, -1)],  # 좌
        [(1,1), (0,1) ,(-1,1)], # 우


    ]
    seen_area = []
    visted = set()
    queue = collections.deque()
    cur_r,cur_c = r,c
    for i in range(3):
        new_r, new_c = cur_r + seen_dir_list[seen_dir][i][0], cur_c + seen_dir_list[seen_dir][i][1]
        if check_B(new_r, new_c, N):
            queue.append((new_r,new_c))
            visted.add((new_r,new_c))
            seen_area.append((new_r,new_c))

    while queue:
        cur_r,cur_c = queue.popleft()
        for i in range(3):
            new_r,new_c = cur_r+seen_dir_list[seen_dir][i][0],cur_c+seen_dir_list[seen_dir][i][1]
            if check_B(new_r,new_c,N) and (new_r,new_c) not in visted:
                queue.append((new_r,new_c))
                seen_area.append((new_r,new_c))
                visted.add((new_r,new_c))
    return seen_area

def check_bar_seen_up(N,M_r,M_c,war_pos,seen_a,M_seen_dir):
    tot_seen_dir_list = { # 가로막아지는 방향
      0:[ # 상
        [(-1, 0),(-1,0)],
        [(-1,0), (-1,-1)],
        [(-1, 0), (-1,1)],
      ],
      3:[ # 우
          [(0, 1),(0, 1)],
          [(0, 1) ,(-1, 1)],
        [(1, 1) ,(0, 1) ],
    ],
      1:[ #하
          [(1, 0),(1, 0)],
          [(1, -1) ,(1, 0) ],
          [(1, 0) , (1, 1)   ],
      ],
      2:[ #좌
          [(0, -1),(0, -1)],
          [(0, -1) ,  (-1, -1)],
          [(1, -1) , (0, -1) ]
      ],
    }
    block_seen_area = []
    visted = set()

    can_block_pos = []

    for po in war_pos: # 모든 war를 확인하면서
        if po in seen_a: # 만약 시야에 들어오는 경우
            depen_dir = 0
            if M_seen_dir == 0 or M_seen_dir==1: # 상하
                if po[1] == M_c:
                    depen_dir = 0
                elif po[1] < M_c:
                    depen_dir = 1
                else:
                    depen_dir = 2
            elif M_seen_dir==2 or M_seen_dir==3: #좌우
                if po[0] == M_r:
                    depen_dir = 0
                elif po[0] < M_r:
                    depen_dir = 1
                else:
                    depen_dir = 2
            #경우에 따라 어느 방향을 막을 수 있는지 확인 후
            can_block_pos.append((po[0],po[1],depen_dir)) # 현재의 위치와 막는 방향을 넣는다.


    seen_dir_list = tot_seen_dir_list[M_seen_dir] # 전사가 막는 방향에 대핸 리스트 메두가사 보는 방향에 따라 다르다

    for pos in can_block_pos: # 시야에 들어가는 전사들 중
        cur_r,cur_c ,seen_dir = pos
        if (cur_r,cur_c) in visted: #이미 막는 시야각에 들어온 경우는 pass
            continue
        queue = collections.deque()
        for i in range(2): # 막는 방향을 구한다. 처음 위치는 들어가지 않는다.
            new_r, new_c = cur_r + seen_dir_list[seen_dir][i][0], cur_c + seen_dir_list[seen_dir][i][1]
            if check_B(new_r, new_c, N):
                queue.append((new_r, new_c,seen_dir))
                visted.add((new_r, new_c))
                block_seen_area.append((new_r, new_c))

        #시야구하기: 나의 위치에서 보는 방향(2~3) 으로 new_r,new_c를 구한다.
        # 그 것을 기반으로 하여 똑같이 보는 방향을 update한다. 이미 본 위치의 경우 다시 보지 않는다.
        # 나의 위치가 포함되지는 않아야한다.

        while queue: # 막는 방향을 update 한다.
            cur_r, cur_c,seen_dir = queue.popleft()
            for i in range(2): #양방향으로 계속 넣는다. 메두사의 시야를 구하는 방식과 동일하다.
                new_r, new_c = cur_r + seen_dir_list[seen_dir][i][0], cur_c + seen_dir_list[seen_dir][i][1]
                if check_B(new_r, new_c, N) and (new_r, new_c) not in visted:
                    queue.append((new_r, new_c,seen_dir))
                    block_seen_area.append((new_r, new_c))
                    visted.add((new_r, new_c))

    return block_seen_area

def make_tot_seen_area(seen_a,block_seen_a):
    new_seen_a = [po for po in seen_a if po not in block_seen_a]
    return  new_seen_a

def make_non_stone_war_list(war_pos,tot_seen_area): #두마리도 들어가는지 확인해야한다.
    non_stone_war_list = []
    for po in war_pos: #전체 기사들을 보는데
        if po in tot_seen_area: #만약 돌이 된 곳이라면 건너뛴다.
            continue
        non_stone_war_list.append(po) # 아닌 경우에는 +
    return  non_stone_war_list

def count_stone_count(war_pos,non_stone_war_list):
    return abs(len(non_stone_war_list)-len(war_pos))

def compute_man_dist(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1-c2)

def take_dist_arr(N,G_r,G_c,arr): # 공원에서 시작해 메두사까지의 거리 리스트를 구해서 반환한다.

    move_dir = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]

    dis_arr = [[float('inf')]*N for _ in range(N) ]
    dis_arr[G_r][G_c] = 0
    queue = collections.deque()
    visted = set()
    visted.add((G_r,G_c))
    queue.append((G_r,G_c))

    while queue:
        cur_r,cur_c = queue.popleft()
        cur_dis = dis_arr[cur_r][cur_c]
        for move in move_dir:
            nr,nc = cur_r+move[0],cur_c+move[1]
            if check_B(nr,nc,N) and (nr,nc) not in visted and arr[nr][nc]==0:
                visted.add((nr,nc))
                queue.append((nr,nc))
                dis_arr[nr][nc] = cur_dis+1

    return  dis_arr

def war_move(N,war_po,M_r,M_c,tot_seen_a):
    #전사를 한칸 이동시킨다. 거리가 짧아지는, 안벗어나는+ 시야에 안들어오는
    move_dir = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    cur_r,cur_c = war_po
    cur_dist =  compute_man_dist(cur_r,cur_c,M_r,M_c)
    next_po = war_po
    for move in move_dir:
        nr, nc = cur_r + move[0], cur_c + move[1]
        dist = compute_man_dist(nr, nc,M_r,M_c)
        if check_B(nr,nc,N) and dist < cur_dist and (nr,nc) not in tot_seen_a:
            next_po = (nr,nc)
            cur_dist = dist
    return next_po

def take_war_move(war_pos,non_stone_war_pos,M_r,M_c,N,tot_seen_a):
    #움직인 거리를 구한다. 전사들의 거리를 update 한다.
    tot_move_dist = 0




    for i in range(len(war_pos)):
        po = war_pos[i]
        cur_dist = compute_man_dist(po[0],po[1],M_r,M_c)
        if po in non_stone_war_pos: #돌이 안된 경우에.
            new_po = war_move(N, po, M_r, M_c, tot_seen_a)
            new_po = war_move(N, new_po, M_r, M_c, tot_seen_a)
            tot_move_dist += (cur_dist - compute_man_dist(new_po[0],new_po[1],M_r,M_c))
            war_pos[i] = new_po
    return war_pos,tot_move_dist

def take_death_war(war_pos,M_r,M_c):
    #마지막에 죽은 전사수를 구한다. 살아남은 전사 리스트를 반환한다.
    new_pos = []
    death_count = 0
    for po in war_pos:
        if po == (M_r,M_c):
            death_count+=1
        else:
            new_pos.append(po)
    return new_pos,death_count

def medusa_move(dist_Arr,sr,sc,war_pos,N):
    move_dir = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    cur_dist = dist_Arr[sr][sc]
    next_po = (sr,sc)
    for move in move_dir:
        nr,nc = sr+move[0],sc+move[1]
        if check_B(nr,nc,N):
            next_dist = dist_Arr[nr][nc]
            if cur_dist>next_dist: # 작은 부분 실수 조심 -> 좌표는 update했으나 위치를 update 안했다.
                next_po = (nr,nc)
                cur_dist = next_dist
    war_pos,death_count  = take_death_war(war_pos, next_po[0], next_po[1])
    return next_po,war_pos,death_count

def det_dir(war_pos,cr,cc,N):

    cur_stone_count = 0
    tot_dir = 0
    tot_none_stone_pos = []
    tot_seen_area = []

    for seen_dir in range(4):
        seen_a = make_first_seen(seen_dir, N, cr, cc)
        block_seen_a = check_bar_seen_up(N, cr, cc, war_pos, seen_a, seen_dir)
        tot_seen_a = make_tot_seen_area(seen_a, block_seen_a)
        non_stone_war_list = make_non_stone_war_list(war_pos, tot_seen_a)
        stone_count = count_stone_count(war_pos, non_stone_war_list)
        if stone_count > cur_stone_count: # 가장 많이 돌이 되는 경우
            cur_stone_count = stone_count
            tot_dir = seen_dir
            tot_seen_area = tot_seen_a #전체 시야
            tot_none_stone_pos = non_stone_war_list # 돌이안된 기사 리스트

    return cur_stone_count,tot_seen_area,tot_none_stone_pos # 돌만든 수, 전체시야, 돌이안된 기사 리스트 반횐


def game_logic(G_r,G_c,sr,sc,arr,N,war_pos):
    dist_arr = take_dist_arr(N,G_r,G_c,arr)



    if dist_arr[sr][sc] == float("inf"):
        print(-1)
        return
    cr,cc = sr,sc
    while True:

        cur_move_count,cur_stone_count,cur_death_count = 0,0,0

        next_po,war_pos,death_count = medusa_move(dist_arr, cr,cc, war_pos, N) #메두사가 이동한다.


        if next_po == (G_r,G_c):
            print(0)
            break

        cr, cc = next_po

        cur_stone_count,tot_seen_area,tot_none_stone_pos = det_dir(war_pos,cr,cc,N) # 방향을 결정하고 바라본다.

        war_pos,tot_move_dist = take_war_move(war_pos, tot_none_stone_pos, cr, cc, N, tot_seen_area)
        cur_move_count += tot_move_dist
        war_pos,death_count = take_death_war(war_pos,cr, cc)
        cur_death_count += death_count
        print(cur_move_count, cur_stone_count, cur_death_count)


N,M = map(int,input().split())
sr,sc,gr,gc=map(int,input().split())
w_a = list(map(int,input().split()))
war_pos = [(w_a[i],w_a[i+1]) for i in range(0,M*2,2)]

arr = [list(map(int,input().split())) for i in range(N)]
game_logic(gr,gc,sr,sc,arr,N,war_pos)


'''
N = 9
seen_dir = 2
M_r,M_c = 0,4
seen_a = make_first_seen(seen_dir,N,M_r,M_c)
print_seen_area(seen_a,N)
war_pos = [(4,2),(4,4),(6,6),(4,2),(5,2),(6,4)]
block_seen_a = check_bar_seen_up(N,M_r,M_c,war_pos,seen_a,seen_dir)
print_seen_area(block_seen_a ,N)
tot_seen_a = make_tot_seen_area(seen_a,block_seen_a)
print_seen_area(tot_seen_a ,N)
non_stone_war_list = make_non_stone_war_list(war_pos,tot_seen_a)
print(count_stone_count(war_pos,non_stone_war_list))

new_po = war_move(N, (0,0), M_r, M_c, tot_seen_a)
new_po = war_move(N, new_po, M_r, M_c, tot_seen_a)
print(new_po)
'''





















