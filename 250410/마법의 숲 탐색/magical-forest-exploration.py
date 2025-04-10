'''
RxC 마법숲 탐색
가장 위를 1행 가장 애래를 R행
동서남은 막혀있다. 북쪽을 통해서만 들어온다
K명의 정령이있다. 각자 골렘잉ㅆ다.
골렘은 십자모양이며 중앙칸을 4칸중 한칸은 출구다
어떤 방향에서든 골렘을 탑승할 수 있다.
그러나 내릴때는 출구를 통해서만 내릴 수 있다.

i번째 골렘은 중앙이 i열이 되도록 내려온다.

골렘의 이동
1. 내려가기:
2. 1을 못하면 서쪽으로 회전하며 내려간다
3. 2를 못하면 동쪽으로 회전하며 내려간다.
회전할때마다 출구 방향이 바뀐다.

골렘이 최대한 남쪽으로 이동했지만 몸의 일부가 밖인 경우
=> 모든 골렘을빼고  다시 시작 . 최종위치에는 포함 안시킨다.

숲의 가장 북쪽에서 시작해서 내려온다.
=> 골렘이 위에서부터 몸을 돌리면서 내려올 수 도 있어야한다
모든 칸이 꽉차있을때 기준을 생각해야한다.


----------------------
전체 로직
골렘을 아래로 내린다.
 1. 이동가능한지 확인한다.
  (1) 남쪽이동 => 중앙을 기준으로 -
  (2) 서쪽 이동 => 중앙을 기준으로
  (3) 동쪽 이동 => 중앙을 기준으로
  가능한 것으로 이동한다.
 2. 정령을 이동시킨다.
   -> 위치를 기준으로 상하좌우 움직일 수 있다. 출구를 통해서만 다른 골렘으로 이동이 가능하다.
   => 골렘끼리 구분을 해야한다. + 출구를 표시해두어야한다. 그러나 이걸 문자열로 두면 안된다. 어려워진다. => 출구만 다른 좌표 표현
   or 격자에 표시
 3. 가장 높은 행을 더한다.
cif1) 가장 북쪽에서 부터 내려온다. 테트리스처럼 쌓일 수 있음을 주의한다.
cif2) 출구를 조심한다. 회전하는 것을 유의한다.
----------------------

필요함수와 map
벽을 1로 표시한다
골렘은 2부터 시작을 한다.
0. init_map => R+5,C+2기준으로 만들기. -> ok
1. 정령의 이동을 표현할  map, R보다는 휠씬 커야한다. 1행의 기준을 새롭게 잡아야한다. -> ok
2. 정령 이동전 탐색 - 남쪽 탐색, 서쪽 탐색, 동쪽 탐색 => map을 기준으로 탐색한다. 중앙 좌표만 이동 시킨다. => ok
   1) 남쪽 탐색 => 벽에 붙어서 가능 경우도 생각해야한다.
     (center_r,center_c) 기준
     이동 가능
     :
   2) 서쪽 탐색 and 남쪽 탐색 => 맨위에서도 회전이 가능해야한다.
   3) 동쪽 탐색 and 남쪽 탐색
   탐색후 r,c를 새로 update한다.
3. 골렘의 표현 => ok
   골렘의 이동을 중앙 좌표로 표현한다. 마지막 칸에 도착하면 map에 그린다.  출구역시 가지고 있다.
4. 정령의 이동
   (map기준)같은 칸에서는 자유럽게 움직인다. 다른칸으로 움직이려고 할때 그 칸이 출구칸인지 확인한다. 그 후 다른 칸으로 이동한다.
   이때 본인이 밟고 있는 칸에 대한 정보(ex:2골렘->3골렘 이동시 2골렘 출구인지 확인 -> 3골렘이동. 현재 3골렘임을 표시)
5. 골렘의 이동. r,c를 구하고 그린다. => ok
6. 골렘 비우기. => 이동을 끝냈는데. 특정 경계 위로 있는 경우 비우기
7. 점수 계산 함수
8. 회전시 출구도 회전되게 해야한다. 출구좌표는 어떻게 바뀌는가.
그냥 상좌하우로 출구의 위치를 받아두고. 회전시 방향을 돌리기 -> 맨마지막 고정시 출구좌표를 구하고 fix시킨다.
test 해야할 것
1. 골렘이 잘 이동하는가. 쭉 내려오기, 피해서 내려오기 등.
2. 골렘이 쌓여있어도 잘 이동하는지
3. 정령이 원하는 칸으로 이동하는지 확인.
조심해야하는 예외
arr에서의 표현, 출구칸 따로 두기 - 골렘 num - 출구
'''


move_dir =[#상우하좌
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]

def init_start_map(R,C):
    new_arr = [ [0]*(C+2) for r in range(R+5)]
    for r in range(R+5):
       new_arr[r][0] = 1
       new_arr[r][C+1] = 1
    for c in range(C+2):
        new_arr[R+4][c] = 1
    return  new_arr

def print_arr(arr):
    for row in arr:
        print(*row)

def seek_s(r,c,arr):
    # 남쪽 탐색.
    # (r+2,c) ,(r+1,c-1) (r+1,c+1) 이 모두 0이어야한다.
    return (arr[r+2][c] == 0 and arr[r+1][c-1]==0 and arr[r+1][c+1]==0)
def seek_w(r,c,arr):
    #서쪽 탐색
    # (r,c-2) (r-1,c-1) (r+1,c-1) 이 모두 0이어야한다.
    return  (arr[r][c-2] == 0 and arr[r-1][c-1]==0 and arr[r+1][c-1]==0)
def seek_e(r,c,arr):
    #동쪽 탐색
    # (r,c+2) (r-1 c+1), (r+1,c+1) 이 모두 0이어야한다.
    return (arr[r][c+2] ==0 and arr[r-1][c+1] ==0 and arr[r+1][c+1] == 0)

def golem_move(gr,gc,de_dir,arr): # 상좌우하
    c_gr,c_gc,c_de_dir = gr,gc,de_dir
    while True:
        if seek_s(c_gr,c_gc,arr):
            c_gr += 1
        elif seek_s(c_gr,c_gc-1,arr) and seek_w(c_gr,c_gc,arr):
            c_gr += 1
            c_gc -=1
            c_de_dir = c_de_dir -1 if c_de_dir >0 else 3
        elif seek_s(c_gr,c_gc+1,arr) and seek_e(c_gr,c_gc,arr):

            c_gr += 1
            c_gc += 1
            c_de_dir = c_de_dir + 1 if c_de_dir < 3 else 0
        else:
            break
    return c_gr,c_gc,c_de_dir
def draw_golem(arr,r,c,g_num):

    arr[r][c] = g_num
    for i in range(4):
        nr,nc = r+move_dir[i][0],c+move_dir[i][1]
        arr[nr][nc] = g_num
    return arr

def make_golem_dic(r,c,g_num,dir_,golem_dic):
    new_golem_exit_dic = golem_dic
    golem_dic[g_num] = {
        "center":(r,c),
        "exit":(r+move_dir[dir_][0],c+move_dir[dir_][1])
    }
    return new_golem_exit_dic

def fary_move(g_num,golem_dic,arr):
    cr,cc = golem_dic[g_num]["center"]
    cur_num = g_num
    visted = set()
    max_node=[cr,cc]

    def dfs(r,c,v):

        if (r,c) in visted or arr[r][c]==1 or arr[r][c]==0:
            return

        visted.add((r,c))
        if max_node[0] < r:
            max_node[0],max_node[1] = r,c

        for move in move_dir:
            nr,nc = r+move[0],c+move[1]
            if arr[nr][nc]==v:
                dfs(nr,nc,v)
            else:
                if (r,c) == golem_dic[v]["exit"]: # 위에서 and로 엮으면 안된다.
                    dfs(nr, nc, arr[nr][nc])


    dfs(cr,cc, g_num)
    return max_node



def make_simul_print_arr(arr,golem_dic):
    print(golem_dic)
    for i in range(len(arr)):
        print(i,end="- ")
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()
    print("c- ",end="")
    for c in range(len(arr[0])):
        print(c,end=" ")




def empty_arr(R,C):
    return init_start_map(R,C)

def game_logic(R,C,K,f_info):
    arr = init_start_map(R,C)
    golem_dic = {}
    ans = 0
    for k in range(K):
        g_num = k+2
        r, c, d = golem_move(0, f_info[k][0], f_info[k][1], arr)
        if r<5:
            arr = empty_arr(R, C)
            continue
        arr = draw_golem(arr, r, c, g_num)
        golem_dic=make_golem_dic(r, c, g_num, d, golem_dic)
        ans+= (fary_move(g_num, golem_dic, arr)[0]-3)

        #print("#test",k)
        #make_simul_print_arr(arr,golem_dic)
    
    print(ans)
R,C,K = map(int,input().split())
f_info = [list(map(int,input().split())) for k in range(K)]
game_logic(R,C,K,f_info)


'''
arr = init_start_map(5,6)

r,c,d = golem_move(0,3,0,arr)
arr= draw_golem(arr,r,c,2)
make_golem_dic(r,c,2,d,golem_dic)
print_arr(arr)
print("================")
r,c,d = golem_move(0,3,0,arr)
arr= draw_golem(arr,r,c,3)
make_golem_dic(r,c,3,d,golem_dic)
print_arr(arr)
print("================")
print(golem_dic)
make_simul_print_arr(arr)
print()
print(fary_move(3,golem_dic,arr))
'''

















