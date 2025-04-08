'''
1~6 숫자가 그려진 nxn 격자판에
1x1크기인 정육면체가 있다.
해당 격자에서 정육면체를 굴린다.
1~6 숫자가 있으며
합이 7이다.
1-6
2-5
3-4
m번에 걸쳐 주사위를 굴린다. 1칸씩
(0,0) 에 있고 오른쪽(col+1)로 움직인다. (init)
이동시
=> 격자를 벗어나면 반대방향으로 움직인다.
움직일때마다 같은 숫자 path로 점수를 얻는다.
2*그 path 개수 만큼

이동 후
밑칸이랑. 현재격자칸이랑 비교
1) 같다면 그대로 방향 유지
2) 밑칸이 격자칸보다 크면 시계방향으로 90도 회전
3) 밑칸이 격자칸보다 작다면 반시계방향으로 90도 회전
다시 굴리기.


--------------------------
프로그램 흐름
주사위를 굴린다.
 =>벗어날 경우 방향을 바꾼다.
점수를 계산한다.
 => 격자의 칸을 dfs로 같은 거 탐색한다.
다음 방향을 정한다.

도형에 관한 내용은 그리면서 하자.

--------------------------
구현해야하는 내용
1. 주사위. 6면 => ok
2. 주사위와 방향과 이동. => ok
3. 격자의 점수 계산. => ok
나머지는 쭉 반복하면 될 듯하다.
-------------------------
주사위 구현하기.
주사위는 방향이 있고 해당방향으로 구르면 바라보는 면의 값이 달라진다.
6면으로 구성되어있다.

절대적으로 고정시켜두가 값만 달라지게 하자
"U" - "D"
"F" - "B"
"R" - "L"

구르는 방향: 4가지.
방향- 상우하좌.

'''
DICE = {
    "U":1,
    "D":6,
    "F":2,
    "B":5,
    "R":3,
    "L":4
}
move_dir = [
    (-1, 0),  # 상
    (0, 1),  # 우
    (1, 0),  # 하
    (0, -1),  # 좌
]
def Roll_DICE(dir,DICE):
    temp_DICE = {}
    if dir == 0:
        temp_DICE["U"],temp_DICE["D"] = DICE["F"],DICE["B"]
        temp_DICE["F"], temp_DICE["B"] = DICE["D"], DICE["U"]
        temp_DICE["R"],temp_DICE["L"] = DICE["R"],DICE["L"]
    elif dir == 2:
        temp_DICE["U"], temp_DICE["D"] = DICE["B"], DICE["F"]
        temp_DICE["F"], temp_DICE["B"] = DICE["U"], DICE["D"]
        temp_DICE["R"], temp_DICE["L"] = DICE["R"], DICE["L"]
    elif dir == 1:
        temp_DICE["U"],temp_DICE["D"] = DICE["L"], DICE["R"]
        temp_DICE["R"],temp_DICE["L"] = DICE["U"],DICE["D"]
        temp_DICE["F"],temp_DICE["B"] = DICE["F"],DICE["B"]
    elif dir == 3:
        temp_DICE["U"], temp_DICE["D"] =  DICE["R"],DICE["L"]
        temp_DICE["R"], temp_DICE["L"] = DICE["D"],DICE["U"]
        temp_DICE["F"], temp_DICE["B"] = DICE["F"], DICE["B"]
    return temp_DICE
def check_N(r,c,N):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return  False

def DICE_MOVE(r,c,dir,N):

    ref_dir = [2,3,0,1] # 반대로 돌아가는 경우. 리스트에 바꿔야하는 방향 index를 넣어두면 간결하게 사용가능하다.
    # 0<->2 // 1<->3

    nr,nc,ndir = move_dir[dir][0]+r,move_dir[dir][1]+c,dir
    if not check_N(nr,nc,N):
        ndir = ref_dir[dir]
        nr, nc = move_dir[ndir][0] + r, move_dir[ndir][1]+c
        return nr,nc,ndir
    return nr,nc,ndir

def cal_score(r,c,arr,N):

    val = arr[r][c]

    visted = set()
    path = []

    def dfs(r,c,val,path):
        if not check_N(r,c,N) or (r,c) in visted or arr[r][c] != val:
            return
        path.append((r,c))
        visted.add((r,c))
        for i in range(4):
            nr,nc=r+move_dir[i][0],c+move_dir[i][1]
            dfs(nr, nc, val,path)
    dfs(r,c,val,path)
    return len(path)

def game_logic(N,M,arr):
    cur_dice_info = (0,0,1)
    score = 0
    DICE = {
        "U": 1,
        "D": 6,
        "F": 2,
        "B": 5,
        "R": 3,
        "L": 4
    }

    for m in range(M):
        cur_r,cur_c,cur_dir = cur_dice_info

        cur_dice_info = DICE_MOVE(cur_r,cur_c,cur_dir, N)
        next_r, next_c, next_dir = cur_dice_info
        DICE = Roll_DICE(next_dir, DICE)

        score += (cal_score(next_r, next_c, arr, N)*arr[next_r][next_c])

        if arr[next_r][next_c] > DICE["D"]:
            next_dir = next_dir - 1 if next_dir >0 else 3
        elif arr[next_r][next_c] < DICE["D"]:
            next_dir = next_dir + 1 if next_dir < 3 else 0
        cur_dice_info = (next_r,next_c,next_dir)
    print(score)

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
game_logic(N,M,arr)











