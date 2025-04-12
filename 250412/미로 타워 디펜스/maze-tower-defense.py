'''
25.04.12 start
문제이해
nxn 격자 1,1~N,N
가운데에 상어가 있음
토네이도 모양으로 칸이 있고 벽이 있다.
각 칸에는 구슬이 들어간다.
구슬은 1,2,3번까지 있다. 연속하는 칸이 있으면 연속하는 구슬이라고한다.

1. 마법시전
블라자드 시전. di(1(상),2(하),3(좌),4(우)) si
di방향 si 이하인 모든칸의 구슬을 파괴하고
그칸은 빈칸이되며 벽은 파괴되지 않는다.

2. 구슬 이동
파괴된 후 구슬은 다시 나선방향으로 이동한다.

3. 구슬 폭발
이때 연속되는 구슬이 있으면 폭발한다. 4개이상
더이상 폭발하는 구슬이 없을때 까지 반복 한다.

4. 구슬 변화
연속하는 구슬(하나도 연속하다고 본다)은
하나의 그룹이라고 한다. 하나의 그롭은 두개의 구슬
A와 B로 변한다. 구슬A의 번호는 그룹에 들어있는 구슬의 개수이고
B는 그룹을 이루고 있는 구슬의 번호이다.
구슬은 다시 그룹의 순서대로 1번칸부터 차례대로 A,B의 순서대로 칸에 들어간다.

만약 구슬이 칸의 수보다 많이 칸에 들어가지 못하는 경우
그 구슬들은 사라진다.


-----------------------------------
로직:
1. 마법시전 -> 구슬을 없앤다
2. 구슬 이동 -> map에 따라 구슬을 이동시킨다
3. 구슬 폭발. 4연속이상의 구슬을 폭발시킨다. 다 폭발 시키고
3-1 다시 구슬을 이동
3-2 다시 구슬 폭발 -> 없을때까지 반복
4. 구슬 변화. 그릅체크 후 구슬쪼개기.
=> 구슬을 일일이 넣자.
-----------------------------------
주요구현
1. 구슬 map 구현하기.! 이게 핵심이다.
arr인데 나선모양으로 벽이 있어야함 ->
정확히는 나선 모양으로 구슬이 들어가야한다!
나선 모양으로 연속된 것을 확인할 수 있어야한다!

방법
- 미리 path를 구해두기 -> 나서의 path.
- break point 표시해두기. (0,0) -> n/2,n/2 까지의 이동.
값 탐색: path를 따라가면서 연속된거 확인 -> path 저장 그 path의 값 0으로
값 이동: 0이면 0 안나올때까지 path상에서 바꾸면서 이동하기.
'''

def check_B(r,c,N):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    return False

def print_arr(arr):
    print("<<=======================")
    for row in arr:
        print(*row)
    print("=======================>>")

def make_tor_path(N):

    arr = [[0]*N for i in range(N)]
    tor_path = []
    move_dir = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0),
    ]
    visted = set()
    cr,cc,cdir = 0,0,0
    visted.add((cr,cc))
    tor_path.append((cr,cc))
    arr[cr][cc] = 0

    for i in range(1,N*N-1):

        nr,nc = move_dir[cdir][0]+cr,move_dir[cdir][1]+cc

        if not check_B(nr,nc,N) or (nr,nc) in visted:
            cdir = cdir+1 if cdir <3 else 0
            nr, nc = move_dir[cdir][0] + cr, move_dir[cdir][1] + cc
        tor_path.append((nr,nc))
        visted.add((nr,nc))
        cr,cc,cdir = nr,nc,cdir
        arr[cr][cc] = i

    #print_arr(arr)
    return tor_path

def put_marble(arr,m_num,tor_path): # m_num을 path에 따라 arr에 넣는다.
    new_arr = [row[:] for row in arr]
    new_pos = (0,0)

    if arr[0][0] !=0: # 모두 들어가 있는 경우
        return new_arr

    for pos in tor_path:
        nr,nc = pos[0],pos[1]
        if new_arr[nr][nc] == 0 :
            new_pos = pos
        else:
            break

    new_arr[new_pos[0]][new_pos[1]] = m_num
    return new_arr

def move_till_marble(arr,tor_path):
    # arr의 모든 구슬을 path안쪽으로 옮김. 중간에 0이 없어야함
    # how? tor_path 뒤어서 부터 따라 간다. 0이 나오면 fix
    # 0이 안나올때까지 간다. 0 이안나오는 순간. 0과 0이 아닌 친구의 위치를 바꾼다. 다음부터 또 실행
    # path는 0,0부터 시작임 따라서 끝점 부터 시작한다.
    # 그점이 0이라면 다음에 0이아닌 걸 찾는다. 둘이 바꾼다.
    # 다시 그 다음 부터 시작한다.

    for i in range(len(tor_path)-1,0,-1):
        pos = tor_path[i]
        #print(arr[pos[0]][pos[1]])
        if arr[pos[0]][pos[1]] != 0:
            continue
        break_pos = tor_path[i]
        for j in range(i-1,-1,-1):
            n_pos = tor_path[j]
            if arr[n_pos[0]][n_pos[1]] !=0:
                break_pos = tor_path[j]
                break

        arr[pos[0]][pos[1]],arr[break_pos[0]][break_pos[1]] = arr[break_pos[0]][break_pos[1]],arr[pos[0]][pos[1]]
    return  arr

def boom_cons_marble(arr,tor_path,boom_mar_list):
    new_arr = [row[:] for row in arr]

    # 연속된 갯수 찾기 => 배열에 넣어두고 확인하는 거
    # 4이상부터 터트릴 수 있다.
    # 그냥 그 point로 부터 진행.
    visted = set()

    is_boom = False

    for i in range(len(tor_path)-1,0,-1):
        pos = tor_path[i]
        cur_v = arr[pos[0]][pos[1]]
        if cur_v == 0 or pos in visted:
            continue
        path_ = [pos]
        visted.add(pos)
        for j in range(i-1,-1,-1):
            n_pos = tor_path[j]
            n_v = arr[n_pos[0]][n_pos[1]]
            if n_v != cur_v:
                break
            path_.append(n_pos)
            visted.add(n_pos)

        if len(path_)>3:
            is_boom = True
            for po in path_:
                var = arr[po[0]][po[1]]
                boom_mar_list[var]+=1
                new_arr[po[0]][po[1]] = 0


    return new_arr,is_boom

def make_cons_group(tor_path,arr):
    cons_group = []
    visted = set()
    for i in range(len(tor_path) - 1, 0, -1):
        pos = tor_path[i]
        cur_v = arr[pos[0]][pos[1]]
        if cur_v == 0 or pos in visted:
            continue
        path_ = [pos]
        visted.add(pos)
        for j in range(i - 1, -1, -1):
            n_pos = tor_path[j]
            n_v = arr[n_pos[0]][n_pos[1]]
            if n_v != cur_v:
                break
            path_.append(n_pos)
            visted.add(n_pos)

        cons_group.append(path_)
    return cons_group

def make_new_mar_using_cons_grop(arr,cons_group):
    new_mar = []
    for group in cons_group:
        A = len(group)
        B = arr[group[0][0]][group[0][1]]
        new_mar.append(A)
        new_mar.append(B)
    return new_mar

def spell_blizard(R,C,dir,S,arr,N, boom_mar_list):
    move_dir = [
        (0, 1),
        (1,0),
        (0, -1),
        (-1,0),


    ]
    cur_r,cur_c = R,C
    for s in range(S):

        nr,nc = move_dir[dir][0]+cur_r,move_dir[dir][1]+cur_c
        if check_B(nr,nc,N):
            var =arr[nr][nc]
            boom_mar_list[var] += 1
            arr[nr][nc] = 0
        cur_r,cur_c = nr,nc
    return arr

def game_logic(init_arr,N,M,magic_info):

    arr = [row[:] for row in init_arr]
    tor_path = make_tor_path(N)
    R,C = N//2,N//2
    boom_mar_list = [0, 0, 0, 0]

    for info in magic_info:
        #print("start!")
        #print_arr(arr)

        dir,S = info
        arr = spell_blizard(R, C, dir, S, arr, N, boom_mar_list)
        #print_arr(arr)
        arr = move_till_marble(arr, tor_path)
        arr,is_boom = boom_cons_marble(arr, tor_path, boom_mar_list)
        while is_boom:
            arr = move_till_marble(arr, tor_path)
            arr, is_boom = boom_cons_marble(arr, tor_path, boom_mar_list)
        cons_group = make_cons_group(tor_path, arr)
        new_mar = make_new_mar_using_cons_grop(arr, cons_group)
        new_arr = [[0] * N for i in range(N)]
        for v in new_mar:
            new_arr = put_marble(new_arr, v, tor_path)
        arr = new_arr
        #print("end!")
        #print_arr(arr)
    ans = 0
    for i in range(1,4):
        ans += boom_mar_list[i]*i

    print(ans)

#다 차있는 경우 에대한 예외처리나 check가 필요할 듯

N,M=map(int,input().split())
init_arr = [list(map(int,input().split())) for i in range(N)]
magic_info = [tuple(map(int,input().split())) for i in range(M)]

game_logic(init_arr,N,M,magic_info)







