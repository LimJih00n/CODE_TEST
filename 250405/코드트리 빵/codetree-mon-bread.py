'''
문제 분석
nxn 칸에서 이루어짐
m명의 사람과 m명의 편의점
베이스 캠프에서 시작 m분일때
베이스 캠프와 편의점은 방문시 벽이 됨
가장 가까운 베이스 캠프에서 시작
가장 가까운 = 벽을 포함해서 상좌우하 로 움직일때 가장 가까운 거리
가장가까운 칸으로 1씩 움직임

생각해야할 것
1. 사람 - 편의점간의 최단 경로 구하기 => 편의점에서 특정칸까지의 최단경로를 구하고 사람이 4칸 중 1칸을 선택해서 이동한다.

구현해야할 함수
1. 편의점 거리 - 다른 곳 거리 구하는 함수
2. 게임 로직 함수
   1) 이동하기 -> 거리 낮은대로 이동
   2) 벽 만들기
   3) base camp 이동하기

필요한 전체 변수
사람 리스트: 사람의 좌표를 담고있다. 0~m-1 까지 순서로 있다.
벽 리스트 : 벽의 좌표를 담고 있다.
편의점 리스트 : i가 i번째 사람이 가야할 편의점이다.
basecamp 리스트 : 그냥 넣어둔다.
성공한 사람 리스트

전체 적 로직
1) 해당 편의점에서 각 칸까지의 거리를 모두 구한다. 해당 사람이 4방 탐색 후 다음칸을 정하고 이동한다. - 사람 편의점은 1:1 대응이므로
2) 도착한 경우에는 다음 벽 리스트에 내용을 추가한다.
3) t<m 일 경우에는 -> 이동해야하는 편의점 - 전체 거리를 구한다. base camp위치와 가까운 곳으로 이동한다. 넣는다.


도착한 사람의 좌표를 알고 있어야한다.
벽칸 사람칸 베이스 캠프 칸 다 볼 수 있게하자.
벽칸을 따로 만들어놔야한다.

사람이 들어가야지 위치가 의미있다. 들어와있는 사람과 아닌 사람을 구분한다.

simul 만들기.

test:
1. 거리를 잘 반환 하는 가


'''
import collections
move_dir = [
    (-1,0),
    (0,-1),
    (0,1),
    (1,0)
]

def check_B(r,c,N):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    return False

def print_arr(arr):
    print("=="*len(arr))
    for row in arr:
        print(*row)

def compute_dist(start_node,N,wall_pos):
    visted = [[False]*N for _ in range(N)]
    visted[start_node[0]][start_node[1]] = True
    queue = collections.deque()
    queue.append(start_node)
    dist_arr = [[0]*N for _ in range(N)]


    while queue:
        cur_node = queue.popleft()

        for i in range(4):
            next_r,next_c = move_dir[i][0]+cur_node[0],move_dir[i][1]+cur_node[1]
            if check_B(next_r,next_c,N) and not visted[next_r][next_c] and (next_r,next_c) not in wall_pos:
                visted[next_r][next_c] = True
                dist_arr[next_r][next_c] = dist_arr[cur_node[0]][cur_node[1]] + 1
                queue.append((next_r,next_c))
    return dist_arr

def game_logic(man_pos,conv_pos,base_pos,wall_pos,N,M):
    alive_pos = []
    t = 0

    while True:

        next_wall_pos = wall_pos[:]
        for i in range(M):
            if man_pos[i] == (-1,-1) or man_pos[i] in alive_pos:
                continue
            dist_arr = compute_dist(conv_pos[i],N,wall_pos)
            cur_node = man_pos[i]
            min_dist = N*N
            next_pos = cur_node
            for j in range(4):
                next_r, next_c = move_dir[j][0] + cur_node[0], move_dir[j][1] + cur_node[1]
                if check_B(next_r,next_c,N) and (next_r,next_c) not in wall_pos and dist_arr[next_r][next_c] < min_dist:
                    min_dist = dist_arr[next_r][next_c]
                    next_pos = (next_r,next_c)
            if next_pos == conv_pos[i]:
                alive_pos.append(next_pos)
                next_wall_pos.append(next_pos)
            man_pos[i] = next_pos

        if t<M:

            dist_arr = compute_dist(conv_pos[t], N, wall_pos)
            min_dist = N * N
            next_pos = base_pos[0]
            for pos in base_pos:
                if dist_arr[pos[0]][pos[1]] < min_dist:
                    min_dist = dist_arr[pos[0]][pos[1]]
                    next_pos = pos
            next_wall_pos.append(next_pos)
            man_pos[t] = next_pos
        wall_pos = next_wall_pos[:]
        t+=1

        if len(alive_pos) ==M:
            break
    return t

def check_conv(arr):
    base_pos = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                base_pos.append((r,c))
    return base_pos
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
conv_pos = [list(map(int,input().split())) for _ in range(M)]
base_pos = check_conv(arr)
man_pos = []
wall_pos = []
for i in range(M):
    conv_pos[i][0] -= 1
    conv_pos[i][1] -= 1
    conv_pos[i] = (conv_pos[i][0],conv_pos[i][1])
    man_pos.append((-1,-1))
#print(conv_pos)
#print(base_pos)
print(game_logic(man_pos,conv_pos,base_pos,wall_pos,N,M))








