'''
25.04.06 start
nxn의 격자에서 진행
술레는 처음에 정중앙에 있다.
m명의 도망자가 있다.
유형은 2가지. 상하로만 or 좌우로만
좌우는 항상 오른쪽 ㅂ고 시작
상하는 항상 아래쪽 보고 시작.
도망자는 중앙에서는 시작안한다.
h개의 나무가 있으며 도망자와 나무가 겹치는 것 가능

도망자 움직이고 슬레 움직이고 가 1ㅓㄴ
도망자는 거리가 3이하인 경우에만 움직임 멘하튼 거리로

움직이는 도망자는
격자를 안벗어나는 경우
 술레가 있다면 안움직임
 해당칸 이동 나무 있어도 ㄱㅊ
격자 벗어나는 경우
 방향반대로 튼다 ->> 이후 방향에 없다면 이동


술레가 움직이는 경우 -> 달팽이 모양 갔다가 다시 돌아옴
이동방향 틀어지는 지점 -> 바로 방향을 틀어줌 => 시야와 관련이 있음
(1,1)에 도달해도 방향바로 틀어야함.
턴 넘기기전 시야내에 있는 도망자를 잡는다.
바라보고 있는 방향의 현재칸을 포함한 3칸
나무랑 같은 칸에 있는 도망자는 못잡음

이동 도중 도망자의 위치가 겹칠 수 있다.


게임 로직
1. 이동가능한 도망자 찾기
2. 이동가능한 도망자 이동 -> 술래 위치에 따라 바뀌는 것 주의
3. 술래 이동(달팽이) -> 시야방향 바꾸는 것 주의.
4. 시야확인 -> 나무있는칸에 있는 사람은 못잡음

반복.

필요함수
1) 이동가능한 도망자 찾기 -> 맨하튼 거리 3
2) 도망자 이동하기 -> pos와 dir을 바꿔야함.
   격자안일때 : 없다면 다음칸이동
   격자밖이면 : 방향전환 후 없다면 다음칸 이동

3) 술래이동
  내가 아는 달팽이 구현 역으로 소용돌이 였음. 문제는 이경우는 한칸씩 시뮬레이션 해야한다는 것.
  물론 경로를 미리 만들어두는 방법도 있다. => 이걸로 하고 꺽는 지점을 표시해두자.
  굳이 그럴 필요 x. 밖에서 보고 가는 경로를 역으로 두면 그게 그거다.

  소용돌이 path k만큼만 필요함. 역배열로 시작.
    # 도착점만 조심하면 될 듯하다.
    # 술래가 움직일때는 역으로 해야함
    # path 하우상좌
    # 술래기준:  가 되야한다. 그리고 역배열탈때는 point 동일함 즉 역배열인지 아닌지를 구분해줘야함 술래의 위치에 따라서
    # 역배열탈때랑 아닐때랑 보는 시야방향이 다르다. 돌아올때는 나가 정한거랑 동일함.
    # 따로 관리하기. braking point로만 사용하기.
    # 문제는 돌아올때 breaking point가 안된다.
    # 역일때는 다음의 break point가 바뀐다면 고개 돌리기
    # 순일때는 현재가 전과 다르다면 고개 돌리기
    # 0:상
    # 3:우
    # 2:하
    # 1:좌
    # (1,1) 과 n//2,n//2마다 바꿔주면 된다.

4) 시야확인 함수
#make_tor_path(3)

#print(seen_sul(0,True,(0,0,True)))
# break point에서 다음칸에 대해
# 보는 방향을 1 늘림.
# 순서기준
# 상 우 하 좌 point에서 하 우 상 좌 point에서 상 우 하 좌
# 보는 view 배열이 바뀜. break point에서는 한칸씩 올림.
# 역이냐 마냐는 저장해야함

# 현재 상황
# break point에서 방향전환. 순이냐, 역이냐에 따라 바라보는 방향 순서 달라짐. point에서 역,순 내용 바뀜
'''
def check_B(r,c,N):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return False

def make_sul_path(K,N):
    s_path = make_tor_path(N)[::-1]
    r_path = s_path[::-1]
    tot_path = []
    now_path = s_path
    i = 0
    # 이어 붙일 경우 중복된다.  중복일경우 건너뀌기.
    cur_p = 1
    path_set = [0,s_path,r_path]
    for k in range(K+1):
        if i == len(s_path):
            i=1
            cur_p *=-1
        tot_path.append(path_set[cur_p][i])
        i+=1
    return tot_path

def make_tor_path(N): # 하우상좌 순
    # 다음 point를 보고 breaking인지?
    path = []
    visted = set()
    move_dir = [
        (1,0),
        (0,1),
        (-1,0),
        (0,-1)
    ]
    dir_count = 0
    r,c,bp = 0,0,True

    test_arr = [[0]*N for i in range(N)]

    for i in range(N*N):
        nr,nc =  r+move_dir[dir_count][0],c+move_dir[dir_count][1]
        bp = False
        if not check_B(nr,nc,N) or (nr,nc) in visted:
            dir_count = dir_count +1 if dir_count <3 else 0
            bp = True
        path.append((r, c, bp))
        visted.add((r, c))
        test_arr[r][c] = i
        nr, nc = r + move_dir[dir_count][0], c + move_dir[dir_count][1]
        r, c, bp = nr, nc, bp

    path[0] = (0,0,True)

    #print_arr(test_arr)

    return path
def print_arr(arr):
    print("=="*len(arr))
    for row in arr:
        print(*row)


# 시야 계산이 너무 복잡하다.
# break point에서 현재 dir에 따라 바꿔주기 시야, 역방향 순방향 보고

def compute_m(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)


def move_runner(runner_po,sul_po,N):

    move_dir = [
        (0,1),
        (0,-1),
        (1,0),
        (-1,0),
    ]

    cur_r,cur_c,cur_dir = runner_po
    nr,nc = cur_r+move_dir[cur_dir][0],cur_c+move_dir[cur_dir][1]
    if check_B(nr,nc,N):
        if (nr,nc) == (sul_po[0],sul_po[1]):
            return (cur_r,cur_c,cur_dir)
        else:
            return (nr, nc, cur_dir)
    else:
        if cur_dir == 0:
            cur_dir = 1
        elif cur_dir == 1:
            cur_dir = 0
        elif cur_dir == 2:
            cur_dir = 3
        elif cur_dir == 3:
            cur_dir = 2
        nr, nc = cur_r + move_dir[cur_dir][0], cur_c + move_dir[cur_dir][1]
        if (nr, nc) == (sul_po[0], sul_po[1]):
            return (cur_r, cur_c, cur_dir)
        else:
            return (nr, nc, cur_dir)

def see_siml(runner_pos,sul_po,tree_pos,N):
    c_arr = [[0]*N for i in range(N)]

    for po in runner_pos:
        c_arr[po[0]][po[1]] = 3
    for po in tree_pos:
        c_arr[po[0]][po[1]] = 1

    c_arr[sul_po[0]][sul_po[1]] = 2



def can_runner_move_check(runner_pos,sul_po,N):


    for i in range(len(runner_pos)):
        pos = runner_pos[i]
        if compute_m(pos[0],pos[1],sul_po[0],sul_po[1]) <=3:

            runner_pos[i] = move_runner(pos, sul_po, N)

    return  runner_pos


def catch_check(sul_po,seen_dir,runner_pos,tree_pos,N,k):
    catch_area = []
    # 나무가 있다면 같은 칸이라고 안잡힌다!

    if (sul_po[0],sul_po[1]) not in tree_pos:
        catch_area.append((sul_po[0], sul_po[1]))

    cur_r,cur_c = sul_po[0],sul_po[1]
    for i in range(2):
        nr,nc = cur_r+seen_dir[0],cur_c+seen_dir[1]

        if check_B(nr,nc,N) and (nr,nc) not in tree_pos:
            catch_area.append((nr,nc))
        cur_r,cur_c = nr,nc
    catch_count = 0
    #print("carr",catch_area)
    #print(catch_count, k, runner_pos)
    for po in runner_pos[:]:
        if (po[0],po[1]) in catch_area:
            runner_pos.remove(po)
            catch_count+=1

    return runner_pos, catch_count*k




def game_logic(sul_path,K,N,runner_pos,tree_pos):

    is_re = False
    seen_dir_not_re = [ # 상 우 하 좌
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]
    seen_dir_yes_re = [ # 하 우 상 좌
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    seen_dir = 0
    dir_count = 0
    tot_score = 0


    for k in range(1,K+1):
        runner_pos = can_runner_move_check(runner_pos, sul_path[k-1], N)
        cur_pos = sul_path[k]
        #see_siml(runner_pos, cur_pos, tree_pos, N)

        if cur_pos[2]:
            dir_count = dir_count+1 if dir_count<3 else 0
        if (cur_pos[0], cur_pos[1]) == (0, 0) and not is_re:
            dir_count = 0
            is_re = True
        if (cur_pos[0], cur_pos[1]) == (N // 2, N // 2) and is_re:
            dir_count = 0
            is_re = False
        if is_re:
            seen_dir = seen_dir_yes_re[dir_count]
        else:
            seen_dir = seen_dir_not_re[dir_count]
        runner_pos, score = catch_check(cur_pos, seen_dir, runner_pos, tree_pos, N,k)
        tot_score += score

        #see_siml(runner_pos, cur_pos, tree_pos, N)

    return tot_score

N,M,H,K = map(int,input().split())
runner_pos = [list(map(int,input().split())) for i in range(M)]
tree_pos = [list(map(int,input().split())) for i in range(H)]
runner_pos = [[po[0]-1,po[1]-1,po[2]] for po in runner_pos]

for i in range(len(runner_pos)):
    pos = runner_pos[i]
    if pos[2] == 1:
        runner_pos[i][2] = 0
    else:
        runner_pos[i][2] = 2
    runner_pos[i] = tuple(runner_pos[i])

tree_pos = [(po[0]-1,po[1]-1) for po in tree_pos]
sul_path = make_sul_path(K,N)
see_siml(runner_pos, sul_path[0], tree_pos, N)
print(game_logic(sul_path,K,N,runner_pos,tree_pos))

