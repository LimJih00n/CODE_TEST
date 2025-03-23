'''
row: R, col: C 
1~R
c<0 and c>C and r>=R 막혀있음
K명의 정령은 골렘을 타고 숲을 탐색한다. => 골렘도 K개
골렘: 4방향, 중앙 (+-1,+-1) and r,c
정해진 출구를 통해 내릴 수 있음
탑승방향은 상관없음
i번째 골렘은 북쪽부터 시작해. 중앙이 c열이 되도록하는 위치에서 내려온다.
(0,ci)에서 내려온다.


골렘 숲 탐색
1) 남쪽으로 한칸 내려간다. r+1,c+1 and r+2 and r+1,c-1이 비었을때
2) 남쪽으로 못내려겨가면 서쪽으로 회전하고 내려간다. 
3) 1x,2x 이면 동쪽으로 회전후 내려감
골렘이 이동할 수 있는 가장 남쪽에 도달할경우 정령은 상하좌우 인접한 칸으로 이동가능
출구가 인접해 있으면 다른 골렘으로도 이동가능 
정령은 이동할 수 있는 칸중 가장 남쪽으로 이동하고 종료=>dfs
이때 위치가 정령의 최종 위치 
정령의 최정위치의 행번호의 합을 구하기. 

골렘 최대한 남쪽으로 이동했지만 숲 밖이라면=. "그 골렘 포함" 다 날려버리고
새롭게 골렘 밑으로 내림 단 이경우네는 정령이 도달하는 최정 위치를 답에 포함 안시킴
=> 날려버린다.=> 다음부터 시작.

cf: 열 더할때 +1 해줘야한다. 1~R이다.

1) 골렘이동 함수. => ok
반환: 골렘의 최종 위치 & 출구위치.
출구가 회전되는 거 주의하기. 
골렘: 중앙 & 몸 & 출구 위치. 
벽에 닿거나.&이동방향으로 갈수있어야함. 다른 골렘에 닿으면 못움직인다. 

골렘의 구성: 좌표 

1)탐색한다.
    2)이동한다.
else
    왼쪽 탐색한다.
    아래쪽 탐색한다.
    방향바꾼다. 
    이동한다. 


1-1) 이동: 보고 있는 방향으로 이동한다. -> 골렘의 좌표에서 행 +1
이동가능한지 확인한다. 
고정되면 고유 number로 표시하기. 출구는 x로 표시하기. 
1-2) 회전: 만약 이동 불가능시 
이동하고
방향 변수 바꾸기
출구 위치 바꾸기
왼쪽으로 돌면: 
오른쪽으로 돌면

gol:
(r,c)
방향
아래:

고려: 정령이 이동할 수 있어야함 + 출구위치가 명확해야함. 
골렘->골렘을 이동할때. -> 다른 골렘임을 표시해줘야함. 

2) 정령 이동 함수 
'''
'''
만들어야하는 함수 => 경계들 확인해야함
1. 골렘이동함수 ok 
2. 정령이동함수 ok 
3. logic 
골렘이동 => 넘어간 거 확인 후 초기화.
정령이동
더하기

이동좌표 확인할때 miss 있었음. 명확하게 세워놓고 교차 검증하기.

0행=>시작위치
1행=>숲
방향에 따른 탐색 => map 확인

남쪽
(r+1,c-1),(r+2,c),(r+1,c+1)
서쪽
(r-1,c-1),(r,c-2),(r+1,c-1)
동쪽
(r-1,c+1),(r,c+2),(r+1,c+1)

회전:
di: 0 1 2 3 북 동 남 서
반시계: di -1
시계:di+1

다 떨어지고 나면 정보 가지고 표시하기. 

숲 밖은 다른 표시 해두기. 
'''


'''
3*3
=>
1   1
1   1
1   1
11111


'''
'''
row: R, col: C 
1~R
c<0 and c>C and r>=R 막혀있음
K명의 정령은 골렘을 타고 숲을 탐색한다. => 골렘도 K개
골렘: 4방향, 중앙 (+-1,+-1) and r,c
정해진 출구를 통해 내릴 수 있음
탑승방향은 상관없음
i번째 골렘은 북쪽부터 시작해. 중앙이 c열이 되도록하는 위치에서 내려온다.
(0,ci)에서 내려온다.


골렘 숲 탐색
1) 남쪽으로 한칸 내려간다. r+1,c+1 and r+2 and r+1,c-1이 비었을때
2) 남쪽으로 못내려겨가면 서쪽으로 회전하고 내려간다. 
3) 1x,2x 이면 동쪽으로 회전후 내려감
골렘이 이동할 수 있는 가장 남쪽에 도달할경우 정령은 상하좌우 인접한 칸으로 이동가능
출구가 인접해 있으면 다른 골렘으로도 이동가능 
정령은 이동할 수 있는 칸중 가장 남쪽으로 이동하고 종료=>dfs
이때 위치가 정령의 최종 위치 
정령의 최정위치의 행번호의 합을 구하기. 

골렘 최대한 남쪽으로 이동했지만 숲 밖이라면=. "그 골렘 포함" 다 날려버리고
새롭게 골렘 밑으로 내림 단 이경우네는 정령이 도달하는 최정 위치를 답에 포함 안시킴
=> 날려버린다.=> 다음부터 시작.

cf: 열 더할때 +1 해줘야한다. 1~R이다.

1) 골렘이동 함수. => ok
반환: 골렘의 최종 위치 & 출구위치.
출구가 회전되는 거 주의하기. 
골렘: 중앙 & 몸 & 출구 위치. 
벽에 닿거나.&이동방향으로 갈수있어야함. 다른 골렘에 닿으면 못움직인다. 

골렘의 구성: 좌표 

1)탐색한다.
    2)이동한다.
else
    왼쪽 탐색한다.
    아래쪽 탐색한다.
    방향바꾼다. 
    이동한다. 


1-1) 이동: 보고 있는 방향으로 이동한다. -> 골렘의 좌표에서 행 +1
이동가능한지 확인한다. 
고정되면 고유 number로 표시하기. 출구는 x로 표시하기. 
1-2) 회전: 만약 이동 불가능시 
이동하고
방향 변수 바꾸기
출구 위치 바꾸기
왼쪽으로 돌면: 
오른쪽으로 돌면

gol:
(r,c)
방향
아래:

고려: 정령이 이동할 수 있어야함 + 출구위치가 명확해야함. 
골렘->골렘을 이동할때. -> 다른 골렘임을 표시해줘야함. 

2) 정령 이동 함수 
'''
'''
만들어야하는 함수 => 경계들 확인해야함
1. 골렘이동함수 ok 
2. 정령이동함수 ok 
3. logic 
골렘이동 => 넘어간 거 확인 후 초기화.
정령이동
더하기

이동좌표 확인할때 miss 있었음. 명확하게 세워놓고 교차 검증하기.

0행=>시작위치
1행=>숲
방향에 따른 탐색 => map 확인

남쪽
(r+1,c-1),(r+2,c),(r+1,c+1)
서쪽
(r-1,c-1),(r,c-2),(r+1,c-1)
동쪽
(r-1,c+1),(r,c+2),(r+1,c+1)

회전:
di: 0 1 2 3 북 동 남 서
반시계: di -1
시계:di+1

다 떨어지고 나면 정보 가지고 표시하기. 

숲 밖은 다른 표시 해두기. 
'''


'''
3*3
=>
1   1
1   1
1   1
11111


'''
'''
row: R, col: C 
1~R
c<0 and c>C and r>=R 막혀있음
K명의 정령은 골렘을 타고 숲을 탐색한다. => 골렘도 K개
골렘: 4방향, 중앙 (+-1,+-1) and r,c
정해진 출구를 통해 내릴 수 있음
탑승방향은 상관없음
i번째 골렘은 북쪽부터 시작해. 중앙이 c열이 되도록하는 위치에서 내려온다.
(0,ci)에서 내려온다.


골렘 숲 탐색
1) 남쪽으로 한칸 내려간다. r+1,c+1 and r+2 and r+1,c-1이 비었을때
2) 남쪽으로 못내려겨가면 서쪽으로 회전하고 내려간다. 
3) 1x,2x 이면 동쪽으로 회전후 내려감
골렘이 이동할 수 있는 가장 남쪽에 도달할경우 정령은 상하좌우 인접한 칸으로 이동가능
출구가 인접해 있으면 다른 골렘으로도 이동가능 
정령은 이동할 수 있는 칸중 가장 남쪽으로 이동하고 종료=>dfs
이때 위치가 정령의 최종 위치 
정령의 최정위치의 행번호의 합을 구하기. 

골렘 최대한 남쪽으로 이동했지만 숲 밖이라면=. "그 골렘 포함" 다 날려버리고
새롭게 골렘 밑으로 내림 단 이경우네는 정령이 도달하는 최정 위치를 답에 포함 안시킴
=> 날려버린다.=> 다음부터 시작.

cf: 열 더할때 +1 해줘야한다. 1~R이다.

1) 골렘이동 함수. => ok
반환: 골렘의 최종 위치 & 출구위치.
출구가 회전되는 거 주의하기. 
골렘: 중앙 & 몸 & 출구 위치. 
벽에 닿거나.&이동방향으로 갈수있어야함. 다른 골렘에 닿으면 못움직인다. 

골렘의 구성: 좌표 

1)탐색한다.
    2)이동한다.
else
    왼쪽 탐색한다.
    아래쪽 탐색한다.
    방향바꾼다. 
    이동한다. 


1-1) 이동: 보고 있는 방향으로 이동한다. -> 골렘의 좌표에서 행 +1
이동가능한지 확인한다. 
고정되면 고유 number로 표시하기. 출구는 x로 표시하기. 
1-2) 회전: 만약 이동 불가능시 
이동하고
방향 변수 바꾸기
출구 위치 바꾸기
왼쪽으로 돌면: 
오른쪽으로 돌면

gol:
(r,c)
방향
아래:

고려: 정령이 이동할 수 있어야함 + 출구위치가 명확해야함. 
골렘->골렘을 이동할때. -> 다른 골렘임을 표시해줘야함. 

2) 정령 이동 함수 
'''
'''
만들어야하는 함수 => 경계들 확인해야함
1. 골렘이동함수 ok 
2. 정령이동함수 ok 
3. logic 
골렘이동 => 넘어간 거 확인 후 초기화.
정령이동
더하기

이동좌표 확인할때 miss 있었음. 명확하게 세워놓고 교차 검증하기.

0행=>시작위치
1행=>숲
방향에 따른 탐색 => map 확인

남쪽
(r+1,c-1),(r+2,c),(r+1,c+1)
서쪽
(r-1,c-1),(r,c-2),(r+1,c-1)
동쪽
(r-1,c+1),(r,c+2),(r+1,c+1)

회전:
di: 0 1 2 3 북 동 남 서
반시계: di -1
시계:di+1

다 떨어지고 나면 정보 가지고 표시하기. 

숲 밖은 다른 표시 해두기. 
'''


'''
3*3
=>
1   1
1   1
1   1
11111


'''
# 이동을 면밀히 안봄
# 출구->출구도 가능하다
# 저런 edge case 생각하기!
def f_move(arr,sr,sc,f_num):
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    visted = set()
    re = []
    
    max_r = 0
    
    def dfs(r,c,f_num):
        nonlocal max_r
        if (r,c) in visted:
            return 
        max_r=max(max_r,r)
        visted.add((r,c))
        re.append((r,c))
        
        for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if arr[nr][nc] == 1 or arr[nr][nc]==0:
                continue
    
            if f_num==arr[nr][nc]:
                dfs(nr,nc,f_num)
            elif arr[nr][nc] == ("x"+str(arr[r][c])):
                
                dfs(nr,nc,f_num)
            elif f_num != arr[nr][nc] and arr[r][c] ==("x"+str(f_num)):
                
                if type(arr[nr][nc]) != str:
                
                    f_num = arr[nr][nc]
                    dfs(nr,nc,f_num)
                    f_num = arr[r][c]
                if type(arr[nr][nc]) == str:
                    f_num = int(arr[nr][nc][1])
                    dfs(nr,nc,f_num)
                    f_num = arr[r][c]
            
            
        
    dfs(sr,sc,f_num)
    
    
    return max_r
                

def print_arr(arr):
    print("="*len(arr))
    for row in arr:
        for v in row:
            print(v,end=" ")
        print()


def init_map(R,C,arr):
    arr = [[0]*(C+2) for i in range(R+2)]
    for c in range(C+2):
        arr[R+1][c] = 1
    for r in range(R):
        arr[r][0] = 1
    for r in range(R):
        arr[r][C+1] = 1
    return arr 
'''
이차원 arr에서도 [-1][-1]이 작동한다..

'''

# 위에서 움직일 수 있는 경우도 생각해야함
# 즉 경계에서 움직이는 경우에 대해서도 생각하기.
def look_s(r,c,arr):
    if c<=0:
        return arr[r+2][c]==0 and arr[r+1][c+1]==0
    if arr[r+1][c-1]==0 and arr[r+2][c]==0 and arr[r+1][c+1]==0:
        return True
    return False
def look_w(r,c,arr):
    
    if r==0:
        return arr[r][c-2]==0 and arr[r+1][c-1]==0
    
    if arr[r-1][c-1]==0 and arr[r][c-2]==0 and arr[r+1][c-1]==0:
        return True
    return False
def look_e(r,c,arr):
    
    if r == 0:
        return arr[r][c+2]==0 and arr[r+1][c+1]==0
    if arr[r-1][c+1]==0 and arr[r][c+2]==0 and arr[r+1][c+1]==0:
        return True
    return False

# 침범하는 경우 발생..

def check_over_for(r):
    if r<2:
        return True
    return False

def golem_move(r,c,dir,arr):
    nr,nc,ndir=r,c,dir 
    while True:
        
        if look_s(nr,nc,arr): # 남쪽으로 이동가능
            nr+=1
        else:
            if look_w(nr,nc,arr) and look_s(nr,nc-1,arr): # 서쪽 탐색
                nr+=1
                nc-=1
                ndir = ndir -1 if ndir >0 else 3
            elif look_e(nr,nc,arr) and look_s(nr,nc+1,arr): # 동쪽 탐색
                nr+=1
                nc+=1
                ndir = ndir+1 if ndir<3 else 0 
            else: # 불가능 
                
                break 
    return nr,nc,ndir

def draw_golem(r,c,dir,gol_num,arr):
    arr[r-1][c] = gol_num
    arr[r+1][c] = gol_num
    arr[r][c-1] = gol_num
    arr[r][c+1] = gol_num
    arr[r][c] = gol_num
    
    if dir==0:
        arr[r-1][c] = "x"+str(gol_num)
    if dir==1:
        arr[r][c+1] = "x"+str(gol_num)
    if dir==2:
        arr[r+1][c] = "x"+str(gol_num)
    if dir==3:
        arr[r][c-1] = "x"+str(gol_num)
    return arr



def game_logic(arr):
    arr = init_map(R,C,arr)
    golem_id = 2
    ans = 0
    for info in golem_info:
        nr,nc,ndir = golem_move(0,info[0],info[1],arr)
        #print(info)
        #print("c",nr,nc)
        if not check_over_for(nr):
            draw_golem(nr,nc,ndir,golem_id,arr)
            #print("Re ",f_move(arr,nr,nc,golem_id))
            ans += (f_move(arr,nr,nc,golem_id))
            golem_id +=1
         #   print_arr(arr)
        else:
            arr = init_map(R,C,arr)
          #  print_arr(arr)
    return ans



R,C,K = map(int,input().split())
arr = [[0]*(C+2) for i in range(R+2)]    
golem_info = [list(map(int,input().split())) for i in range(K)]

print(game_logic(arr))

#print(f_move(arr,nr,nc,5))
#print(sorted(f_move(arr,4,4,4), key = lambda x:-x[0]))
