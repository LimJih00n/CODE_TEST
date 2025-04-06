'''
꼬리잡기 놀이
nxn 놀이 진행
3명이상이 한팀이된다.
맨 앞사람이 머리 뒷사람이 꼬리
주어진 이동선을 따라서만 이동.
이동선 끝은 이어져있고 이동선은 안겹친다.
이동선의 각 칸은 2개의 인점만 존재한다. -> 즉 바로 옆에 이동선이 있는 경우는 없다.

1 1
1 1
  1
인 경우는 없음

라운드
1. 머리사람을 따라서 한칸이동
2.
1~n: 행 커지는 순으로 열 커지게
n+1~2n: 열커지는 순으로 행 작아지게
2n+1~3n: 행 작아지는 순으로, 열 작아지게
3n+1~4n: 열 작아지는 순으로, 행커지게

4n 이후에는 초기화

3. 공이 던져지는 경우 -> "최초"에 만나게 되는 사람만이 공을 얻어
점수를 얻는다. =>이후는 점수 안얻음
머리 사람으로 시작해 k번째 사람이라면 "k의 제곱"만큼 점수를 얻는다.

공을 획득하면 머리사람과꼬리사람이 바뀐다 -> 방향이 바뀐다.

필요함수
(1) 공던지기 함수 ->
    x턴에 따라 공이 이동하기 위한 칸 구하기.
   => 사람 만나면 점수 반환

(2) 사람 이동함수 -> 머리 꼬리 기준으로 사람이동 구하기. -> ok

(3) 방향 바꾸기 함수 -> ok

(4) 공 check 함수

문제: 초기 사람의 좌표들과 순서를 어떻게 담고 있을 것인가.


전체적 로직
1) 사람이동함수로 모든 사람을 경로에 따라 이동시킨다. => ok team 단위로 arr에 넣어두고 이동하기.

문제1: man_pos를 처음에 구해야함. + team에 다라 나눠야함.

2) 공던지기 함수로 공의 이동 괘적을 구한다.
3) 공을 던지고 충돌처리를 한다.
  => 최초의 만나는 사람의 k ** 2 => 구하고 이동방향을 바꾼다. -> 해당 팀의

이동 로직: 이동방향
꼬리잡기 -> head,tail
그 사람이 k번째라는 게 있어야한다.
이동함수: 팀 -> 머리부터 시작해
4를 따라 이동을 해야한다 -> 4방 둘러보고 이동하기. 4일경우
둘이 자리 바꾸기.

경로를 x로 두기
방향을 바꾸는 것을 어떻게 표현 vs k번째를 아는 것에 대한 표현
배열에도 저장, 리스트에도 저장
방향바꿀때마다 역배열로 좌표 바꿔두기.
항상 앞이 head이게
-> 이동은 arr에서 좌표 변환은 pos list에서
i번째(0부터 시작) 에가 i번째 애임


구현1.
이동 로직 정리 => 1 2222 3 으로 arr에는 두기.
man_pos
arr
탐색하면서 4일경우 한칸이동 arr자리 swap, pos update.
당연히 뒤의 4로 갈 수도 있다. 방향에 따라 달라야한다. => 방문한 칸으로만 가야함 첫번째 말고는

'''

def check_b(r,c,N):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return False

def print_arr(arr):
    print("=="*len(arr))
    for row in arr:
        print(*row)



def move_to_line(man_pos,arr,N):

    to_next_r, to_next_c = man_pos[0]
    for i in range(len(man_pos)):
        if i == 0:
            cur_r, cur_c = man_pos[i]
            for sr,sc in zip(dr,dc):
                next_r,next_c = cur_r+sr,cur_c+sc
                if check_b(next_r,next_c,N) and arr[next_r][next_c] == 4:
                    arr[next_r][next_c],arr[cur_r][cur_c] = arr[cur_r][cur_c],arr[next_r][next_c]
                    man_pos[i] = (next_r,next_c)
        else:
            cur_r, cur_c = man_pos[i]
            temp_pos = man_pos[i]
            man_pos[i] = (to_next_r, to_next_c)
            arr[to_next_r][to_next_c], arr[cur_r][cur_c] = arr[cur_r][cur_c], arr[to_next_r][to_next_c]
            to_next_r, to_next_c = temp_pos

    

def change_head(arr,man_pos):
    head_r,head_c = man_pos[0]
    tail_r,tail_c = man_pos[-1]
    arr[head_r][head_c] , arr[tail_r][tail_c] = arr[tail_r][tail_c],arr[head_r][head_c]
    man_pos = man_pos[::-1]
    return man_pos

def find_man_pos(arr,N): # 초기 팀의 모든 좌표를 알아낸다.

    visted = set()

    def dfs(node,path): # dfs node가 찾는게 아니거나 조건에 어긋나면 return
        if node in visted or (not check_b(node[0],node[1],N)) or arr[node[0]][node[1]] == 4 or arr[node[0]][node[1]] == 0:
            return
        path.append(node) # 이후에는 방문에 추가 or 경로에 추가후
        visted.add(node)
        cur_r, cur_c = node
        for sr, sc in zip(dr, dc): # 4방 탐색 후 바로 다음 dfs 진행. bfs랑 다르게 넣기 전에 굳이볼필요x
            next_r, next_c = cur_r + sr, cur_c + sc
            dfs((next_r,next_c),path)


    tot_team = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                path=[]
                dfs((r,c),path)
                tot_team.append(path)
    return tot_team


def ball_move_init(Round,N): # ball의 방향과 시작점을 반환한다.

    mode_Round = Round % N if (Round % N) != 0 else N

    if Round > 4*N:
        Round -= 4*N


    if 1<=Round<=N:
        return mode_Round-1,0,(0,1)
    elif N+1<=Round<=2*N:
        return N-1,mode_Round-1,(-1,0)
    elif 2*N+1<=Round<=3*N:
        return N-mode_Round,N-1,(0,-1)
    elif 3 * N + 1 <= Round <= 4 * N:
        return 0,N-mode_Round,(1,0)

def ball_move(sr,sc,dir,N,tot_team): # 맞춘팀과 점수를 반환한다.
    #처음 맞춘 사람을 못본다.
    score = 0
    cur_r,cur_c = sr,sc
    hit_pos = (-1,-1)
    for i in range(N):

        if arr[cur_r][cur_c] == 1 or arr[cur_r][cur_c] == 2 or arr[cur_r][cur_c] == 3:
            hit_pos = (cur_r,cur_c)
            break

        next_r,next_c = cur_r+dir[0],cur_c+dir[1]

        if not check_b(next_r,next_c,N):
            break
        cur_r,cur_c = next_r,next_c
    hit_team_idx = -1

    if hit_pos == (-1,-1):
        return 0,hit_team_idx


    for team in range(len(tot_team)):
        for t in range(len(tot_team[team])):
            if tot_team[team][t] == hit_pos:
                score = ((t+1)**2)
                hit_team_idx = team
    return score , hit_team_idx

'''
로직전 check
1) 사람 돌리기 잘되는가? -> ok
2) 사람 방향전환 잘 되는가? -> ok
3) 팀 수 잘 구하는가? -> ok
4) round 회전 잘 반영하는가? -> ok
5) 최초사람과 점수, 그 팀을 잘 구하는 가? -> ok

게임 로직

1) 초기팀 좌표를 구한다
2) 게임 simul
- 사람들을 이동시킨다.
- 공 던지는 방향을 구한다. 
- 공을던진다
- 맞춘팀과 점수를 구한다. 총 점수에 더한다.
- 맞춘팀의 방향을 바꾼다. 공백이거나 점수가 0이면 cancel한다. 

'''

def game_logic(N,arr,Round,K):

    tot_score = 0

    tot_team = find_man_pos(arr,N)

    while True:

        for team in tot_team:
            move_to_line(team, arr, N)
        sr,sc,dir= ball_move_init(Round, N)
        score,heat_team_idx= ball_move(sr, sc, dir, N, tot_team)
        tot_score += score
        if heat_team_idx != -1:
            tot_team[heat_team_idx] = change_head(arr,tot_team[heat_team_idx])

        if Round == K:
            break
        Round += 1
    return tot_score

dr = [1,-1,0,0]
dc = [0,0,1,-1]
arr = [
    [2,2,2,1],
    [3,0,0,4],
    [4,0,0,3],
    [1,2,2,2],
]
'''
manpos와 arr만 있으면 해당 man pos 그룹을 이동 + 방향 전환까지 가능해졌다
제일 큰 문제는 man_pos를 구하는 것이다. 어떻게할 수 있을까?
arr에서 1을 찾는다. 4방 탐색후 2나 3을 찾는다. => 다 찾을때까지 반복 => dfs
# dfs로 1에서 시작해 끝날때까지 반복함. 어짜피 1이 처음 시작점이다.  
'''


N,M,K = map(int,input().split())
arr = [list( map(int,input().split())) for i in range(N)]
ans = game_logic(N,arr,1,K)
print(ans)