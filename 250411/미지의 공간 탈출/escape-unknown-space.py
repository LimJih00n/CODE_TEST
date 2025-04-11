'''
문제 해석
----------------------------
nxn 크기의 미지 공간
한변의 길이가 m인 시간의 벽이있다.
2차원 단면도와 시간의 벽의 단변도가 주어지며
0은 빈칸 1은 장애물이다.
타임머신은 시간의 벽 윗면에 있으며 2로 표시된다.
시간의 벽의 위치는 3으로 탈출구는 4로 표시된다.
바닥에는 F개의 시간 이상 현상이 존재한다.
ri,ci에서 시작 vi의 배수마다 방향 di로 한칸씩 확산된다.
확산된 이후에도 남아있다.
장애물, 탈출구 만나면 확산안하고 멈춘다
독립적이며 동시에 확산된다.
동(0)서(1)남(2)북(3)
턴당 타임머신은 상하좌우 1칸. 장애물,ㅡ 시간이상현상 피해야함
필요한 턴수 구하기 없다면 -1
시간 이상현상이 확산된 직 후 이동. 확산된 곳을 못간다.
----------------------------
전체적인 로직
1. 시간 이상 현상을 적용시킨다.
  =>vi 배수턴마다 di로 한칸씩 확산.
2. 타임머신을 이동시킨다.
  bfs => 3d 에서의 bfs.

  bfs 탐색 중에 시간 이동 현상이 포함되어야한다. 전체 map에.

---------------------------
key point: 3d에서의 bfs->3d에서의 map을 구현해야한다.
idea
2차원 arr이 총 6개 있다.
윗면
동서남북
아래평면

서로의 이동이 자연스러워야한다. + 내려갈때 잘 이동이 되야한다.
3d나 구조를 그려야하는 경우는 종이를 적극적 활용하기.

map 정의
0
1 2 3 4
5

1 2 3 4 기준으로
r이 0보다 작아지면 => 0
r이 M>= 되면 => 5


'''
import collections
from turtledemo.penrose import start


def move_new_dem(r,c,dim,M,MR,MC):
    nr,nc,ndim = r,c,dim
    if dim ==0:# 위에서 아래로 내려가능 경우
        if nr<0: # 북
            nr,nc,ndim = 0,M-1-c,3
        elif nr>=M: #남
            nr, nc, ndim = 0, c, 1
        elif nc<0: #서
            nr, nc, ndim = 0, r, 4
        elif nc>=M: #동
            nr, nc, ndim = 0, M-r-1, 2
    elif dim!=5:
        if nc<0: #서로간의 이동
            nc = 0
            ndim = dim-1 if dim >1 else 4
        elif nc>=M:
            nc = 0
            ndim = dim + 1 if dim < 4 else 1
        if nr<0: #위로 다시 올라가는 경우
            if dim == 1:
                nr,nc,ndim = M-1,c,0
            elif dim == 2:
                nr, nc, ndim = M-1-c, M - 1, 0
            elif dim == 3:
                nr, nc, ndim = 0, M - 1 - c, 0
            elif dim==4:
                nr, nc, ndim = c, 0, 0
        elif nr>=M: #아래로 내려가능 경우
            if dim == 1:
                nr,nc,ndim = MR+M,MC+c,5
            elif dim == 2:
                nr, nc, ndim = MR+M-1-c, MC+M, 5
            elif dim == 3:
                nr, nc, ndim = MR-1, MC+M-1-c, 5
            elif dim==4:
                nr, nc, ndim = MR+c, MC-1, 5
    return  nr,nc,ndim

def time_move(r,c,dir,dim_dic):
    move_dir = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
        (0,0)
    ]
    dim_dic[5][r][c] = 1
    nr,nc = r+move_dir[dir][0],c+move_dir[dir][1]
    if dim_dic[5][nr][nc] == 0:
        return nr,nc,dir
    return r,c ,4

def check_B(r,c,N):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return False

def simul(start_node,time_p_list,M,N,MR,MC,GR,GC,dim_dic):
    move_dir = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    visted = set()
    queue = collections.deque()
    visted.add(start_node)
    queue.append((start_node,0))


    while queue:

        cur_node,cur_time = queue.popleft()
        #print("!!",cur_node,cur_time)
        if (cur_node[0],cur_node[1]) == (GR,GC) and cur_node[2]==5:
            #print_suml(dim_dic)
            return  cur_time

        for i in range(len(time_p_list)): # 14가 여러개일 수 있다. 최초의 시간 하나에 대해서만 해야한다.
            p = time_p_list[i]
            if cur_time % p[4] ==0:

                r,c,d = time_move(p[0], p[1], p[2], dim_dic)
                if cur_time == 0:
                    new_t = p[3]
                else:
                    new_t = p[3] + p[4]
                time_p_list[i] = (r,c,d,p[3],new_t)
        cur_r,cur_c,cur_dim = cur_node

        if dim_dic[cur_dim][cur_r][cur_c] == 1:
            continue

        if cur_dim !=5:
            for move in move_dir:
                nr,nc = cur_r+move[0],cur_c+move[1]
                nr,nc,ndim = move_new_dem(nr,nc,cur_dim,M,MR,MC)

                if dim_dic[ndim][nr][nc] != 1 and (nr,nc,ndim) not in visted:
                    visted.add((nr,nc,ndim))
                    queue.append(((nr,nc,ndim),cur_time+1))
        else:
            for move in move_dir:
                nr,nc = cur_r+move[0],cur_c+move[1]
                if  check_B(nr,nc,N) and dim_dic[cur_dim][nr][nc] != 1 and (nr,nc,cur_dim) not in visted:
                    visted.add((nr, nc, cur_dim))
                    queue.append(((nr, nc, cur_dim), cur_time + 1))

    return -1

def print_suml(dim_dic):
    print("===U===")
    for row in dim_dic[0]:
        print(*row)
    print("===S===")
    for row in dim_dic[1]:
        print(*row)
    print("===E===")
    for row in dim_dic[2]:
        print(*row)
    print("===N===")
    for row in dim_dic[3]:
        print(*row)
    print("===W===")
    for row in dim_dic[4]:
        print(*row)
    print("===RE===")
    for row in dim_dic[5]:
        print(*row)

def find_sr_sc(arr):
    for r in range(M):
        for c in range(M):
            if arr[r][c] == 2:
                return r,c
def find_MR_MC(arr):
    for r in range(M):
        for c in range(M):
            if arr[r][c] == 3:
                return r,c
def find_GR_GC(arr):
    for r in range(M):
        for c in range(M):
            if arr[r][c] == 4:
                return r,c

dim_dic = {
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
}


N,M,F = map(int,input().split())
dim_dic[5] = [list(map(int,input().split())) for _ in range(N)]
dim_dic[2] = [list(map(int,input().split())) for _ in range(M)]
dim_dic[4] = [list(map(int,input().split())) for _ in range(M)]
dim_dic[1] = [list(map(int,input().split())) for _ in range(M)]
dim_dic[3] = [list(map(int,input().split())) for _ in range(M)]
dim_dic[0]= [list(map(int,input().split())) for _ in range(M)]
time_p_list = [list(map(int,input().split())) for _ in range(F)]
new_time_p_list = []
for p in time_p_list:
    new_p = [p[0],p[1],p[2],p[3],p[3]]
    new_time_p_list.append(new_p)




sr,sc = find_sr_sc(dim_dic[0])
MR,MC = find_MR_MC(dim_dic[5])
GR,GC = find_GR_GC(dim_dic[5])
start_node = (sr,sc,0)
print(simul(start_node,new_time_p_list,M,N,MR,MC,GR,GC,dim_dic))






















