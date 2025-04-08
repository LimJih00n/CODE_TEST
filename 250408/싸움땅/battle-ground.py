'''
25.04.08-16:40 - 싸움땅

방향을 바꾸면 쭉 이어진다.

nxn 크기의 격자
무기가 있다. 플레이어는 초기능력치가 있다. 다 다르다.
총공격력이 있다.

각 라운드당
보고있는 방향으로 움직인다. (1만큼)
격자를 벋어나는 경우는 반대방향으로 바꾸고 1만큼 이동
이동한 방향에 플레이어가 없다면
  총이 있다면. 가지고 있는 총과 없는 총중에 공격력이 더쎈총 획득
  나머지 총은 격자에 둔다.
플레이가가 잇다면
 싸운다. 초기능력ㅊ+ 총공력랍하 높은 사람이 이김.
         같다면 초기 능력치 높은 사람이 이김
         이긴플레이어는 각 플레이어의(초기능력치+총공격력 합) 점수 얻음
진 플레이어는 총을 내려두고
   보고 있던 칸으로 이동 -> 다른플레이어있거나. 격자범위밖->오른쪽 90도 회전 후이동
   총이있다면 가장 높은 총 얻는다.
이긴 플레이어는
  승리한 칸에 떨어져있는 총"들"과 원래 있던 총중 가장 높은 총 획득하고
  나머지 총들은 격자에 놓는다.

1~n플레이어까지 진행하면 1라운드가 끝난다.
이긴 경우 포인트를 획득.
k 라운드동안 진행하면서 각 플레이거가 획득한 포인트 출력하기.


---게임 로직---
1~n플레이어를 모두 돌면서
플레이어를 이동함수에 따라 이동시킨다. -> 총과 관련해 처리한다.
-> 플레이어가 있다면 배틀을 한다.
-> 진 플레이어는 총을 내려놓는다.
-> 점수를 획득한다.
-> 진 플레이어는 이동함수를 적용시킨다. (90도 회전해야하는 함수)
-> 이긴 플레이어는 다시 총 획득함수를 적용시킨다.

---key function---
1)  싸움 처리 로직
2) 총을 어떻게 관리할 것인가. => 총은 pos에 여러개 있을 수 있음. 총은 pos와 공격력을 가짐. 그 캐릭터가 들면 가지고 움직여야함.
3) 캐릭터 이동 로직. (1) 단순이동, (2) 싸움 후 이동.

핵심은 총을 어떻게 관리할지이다.
1안 nxn - 리스트.
특정 pos에 총이 있는지 확인해야하며. 가장 높은 총을 항상볼 수 있어야한다. -> 까지는 필요없더라도.
nxn pq.

플레이어: r,c,batk,gatk

heapq로 pq 간접적 구현 가능 안의 값이 정렬되어있는 것은 아니다. 단 나오는 값 pop 값이 최대 or 최소를 보장해줄 수 있음
[-1,1] 로 넣으면 내림차순 정렬이가능하다.
삭제를 하지 않고 얻을려면 pq[0] 맨 앞값을 보면 된다.
------------------
만들어야하는 함수
player_list = [r,c,batk,gatk,point] 로 구성.
        0 1   2        3       4     5   6
player: r,c,dir,base_atk,gun_atk,point, idx

1. player 이동함수 -> po를 보는 방향으로 이동시킨다. 벽에 부딫히면 방향바꾸고 한칸 반환한다.
-> po를 반환하기
2. 배틀 함수 -> player 정보 받아서 이긴 player를 반환한다
3. drp함수 플레이어의 총을 떨군다.
4. get 함수 칸ㅇ과 비교해 가장 높은 총을 얻는다.
5. 플레이어는 어떻게 관리할 것인가 and 만나는지를 어떻게 확인할 것인가
player_list로 전체 playrer 관리
meat_player로 1차로 돌면서 만났는지 안만났는지 확인. 만나면 True와 그 player 반환하기. 아니면 False와 나 반환하기.
---------------------------------------------

확인해야하는 거
총을 잘 떨구고 줍는지
이긴player 진 player잘 확인하는 지
이동 잘하는지

'''
import heapq


#import heapq로 heapq넣을 수 있고
#heapq.heapify()로 리스트를 힙화 시킬 수 있음. -> 그 자체가 heap이 된다.

def tot_simul():
    N,M,K = map(int,input().split())
    arr = [list(map(int, (input()).split())) for _ in range(N)]
    player_list = [list(map(int, (input()).split())) for _ in range(M)]
    gun_fight_map = []
    game_logic(player_list, gun_fight_map, N, K, arr)




def print_arr(arr):
    for row in arr:
        print(*row)

def make_simul(player_list,gun_fight_map,N,k):
    print(k," =====================")
    print("======gun====")
    for row in gun_fight_map:
        print(row)
    print("==========player=============")
    c_arr = [[0]*N for _ in range(N)]
    for po in player_list:
        c_arr[po[0]][po[1]] = po[3]
    print_arr(c_arr)
    print("score")
    for po in player_list:
        print(po[5],end=" ")
    print()
    print("=======================")

def print_ans(player_list):
    for po in player_list:
        print(po[5],end=" ")

def init_player_list(player_list): # ok
    new_player_list = []
    idx = 0
    for player in player_list:
        new_player_list.append([player[0]-1,player[1]-1,player[2],player[3],0,0,idx])
        idx+=1
    return  new_player_list


def game_logic(player_list,gun_fight_map,N,K,arr):

    gun_fight_map = make_gun_init_map(arr, N)
    player_list = init_player_list(player_list)


    for k in range(K):
        #print(k,"start!")
        #make_simul(player_list, gun_fight_map, N, k)
        for p in range(len(player_list)):
            player = player_list[p]
            player = player_move(player,N)
            is_meet, m_player = meet_player(player,player_list)

            if not is_meet:
                player,gun_fight_map = drop_gun(player, gun_fight_map)
                player,gun_fight_map = get_gun(player, gun_fight_map)
                player_list[player[6]] = player
            else:
                win_p,lo_p = battle(player, m_player)
                lo_p, gun_fight_map = drop_gun(lo_p, gun_fight_map)
                win_p, gun_fight_map = get_gun(win_p, gun_fight_map)
                #print("W",win_p,"l",lo_p)
                lo_p = move_loose_p(lo_p,N,player_list)
                lo_p, gun_fight_map = get_gun(lo_p, gun_fight_map)
                player_list[win_p[6]] = win_p
                player_list[lo_p[6]] = lo_p
        #print(k, "end!")
        #make_simul(player_list, gun_fight_map, N, k)
    print_ans(player_list)
def move_loose_p(player,N,player_list):
    move_dir = [  # 0,1 상하 / #2,3 좌 우
        (-1, 0),  # 상
        (0, 1),  # 우
        (1, 0),  # 하
        (0, -1),  # 좌

    ]
    cur_r,cur_c,cur_dir = player[0],player[1],player[2]
    nr,nc = cur_r+move_dir[cur_dir][0],cur_c+move_dir[cur_dir][1]
    temp_player = player[:]
    temp_player[0],temp_player[1]=nr,nc
    is_meat,t = meet_player(temp_player, player_list)

    if not is_meat and check_B(nr,nc,N):
        return  temp_player
    else:
        while True:
            n_dir = cur_dir +1 if cur_dir <3 else 0
            nr, nc = cur_r + move_dir[n_dir][0], cur_c + move_dir[n_dir][1]
            temp_player = player[:]
            temp_player[0], temp_player[1],temp_player[2] = nr, nc,n_dir
            is_meat, t = meet_player(temp_player, player_list)
            if not is_meat and check_B(nr, nc, N):
                return temp_player
            cur_dir = n_dir




    return new_player


def meet_player(me_player,player_list):
    cur_po = (me_player[0],me_player[1])

    for p in range(len(player_list)):
        player = player_list[p]
        po = (player[0],player[1])
        if po == cur_po and player[6]!=me_player[6]:
            return  True,player
    return  False,me_player

def make_gun_init_map(arr,N):

    gun_fight_map = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            each_place =[]
            each_place.append((-arr[r][c],arr[r][c]))
            heapq.heapify(each_place)
            gun_fight_map[r][c] = each_place

    return gun_fight_map

def check_B(r,c,N):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return False

def player_turn_find(player): # player의 방향을 바꾼다. -> 이후에 이동을 시켜야한다. 있는지 없는지와 벽도 확인해야한다.
    new_player = player
    new_player[2] = player[2] +1 if player[2] < 3 else 0
    return new_player

def battle(player1,player2): # 이긴 플레이어와 진플레이어를 반환한다.
    p_1_tot_atk = player1[3]+player1[4]
    p_2_tot_atk = player2[3]+player2[4]

    get_point = abs(p_1_tot_atk-p_2_tot_atk)

    if p_1_tot_atk > p_2_tot_atk:
        player1[5] += get_point
        return player1,player2
    elif p_2_tot_atk > p_1_tot_atk:
        player2[5] += get_point
        return player2,player1
    else:
        if player1[3]>player2[3]:
            player1[5] += get_point
            return player1,player2
        else:
            player2[5] += get_point
            return player2,player1


def drop_gun(player, gun_fight_map):  # player가 총을 버린다. 총 map을 update한다.
    new_player = player

    r, c = player[0], player[1]
    if not player[4]:
        return new_player, gun_fight_map

    heapq.heappush(gun_fight_map[r][c], (-player[4], player[4]))
    new_player[4] = 0
    return new_player, gun_fight_map

def get_gun(player, gun_fight_map):  # player가 총을 줍는다. 총 map을 update한다.
    new_player = player
    r, c, cur_gun = player[0], player[1], player[4]

    new_gun = gun_fight_map[r][c][0][1]

    if new_gun > cur_gun:
        new_player[4] = new_gun
        heapq.heappop(gun_fight_map[r][c])
        heapq.heappush(gun_fight_map[r][c], (-cur_gun, cur_gun))
    return new_player, gun_fight_map





def player_move(player,N): # 받는 순간 움직인다.
    move_dir = [ #0,1 상하 / #2,3 좌 우
        (-1,0), # 상
        (0, 1), # 우
        (1,0), #하
        (0,-1), # 좌

    ]
    new_player = player
    nr,nc,ndir = player[0],player[1],player[2]
    nr, nc = player[0] + move_dir[ndir][0], player[1] + move_dir[ndir][1]
    if not check_B(nr,nc,N):
        if player[2] == 2:
            ndir = 0
        elif player[2] == 0:
            ndir = 2
        elif player[2] == 1:
            ndir = 3
        elif player[2] == 3:
            ndir = 1
    nr, nc = player[0] + move_dir[ndir][0], player[1] + move_dir[ndir][1]
    new_player[0],new_player[1],new_player[2] = nr,nc,ndir
    return new_player

tot_simul()
































