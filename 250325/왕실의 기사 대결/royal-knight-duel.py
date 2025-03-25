'''
LxL 체스판
(1,1)에서 시작함
각 칸은 빈칸 함정 벽
밖도 벽으로 간주 => 1로 감싸기

기사: (r,c)위치.  -> h,w 형태의 모양 
                 k의 체력이있음

이동: 상하좌우 중 하나로 이동. 위치에 다른 기사가 있다면 그 기사도 밀려남
뒤에 또있으면 또 밀려남. 이동하는 방향= 벽에 부딭히면 모든 기사의 이동 종료
체스판에서 사라진 기사의 이동은 무시

기사이동 -> 밀쳐짐 -> 밀려난 기사들은 미해를 입는다. 

각 기사들은. 
해당 기사가 이동한 곳에서 wxh 직사각형내에 놓여있는
함정의 수만큼만 피해를 입는다. 각 기사마다 피해를 받은 반큼 체력이 깍인다.
현재체력이상의 대미지=>사라짐 
명령을 받은 기사는 피래를 입지 않는다
기사들은 모두 밀린 이후 대미지를 입는다.
밀렸더라고 밀쳐진 위치에 함정이 없다면 기사는 피해를 입지 않는다. 

생존한 기사들이 받은 데미지의 총합을 구하기. 

만들어야하는하는 함수
1) 기사 이동 함수 (한칸 이동한다. ) 밀쳐짐에 대해서도 확인해야한다. 
 1-1: 명령에 따라 이동 => 벽에 부딭히는지 확인 => 제일 뒤의 기사가 
 벽이 있는지 확인해야함. 
 한칸뒤에 없다면. 한칸씩 이동하기 
 =>모든 기사가 한칸씩 이동가능하면 한칸씩 이동하기 
 1-2: 다른 기사의 움직임 계산. => 벽에 부딫히는지 확인
2) 기사 피해 계산 함수 <- 움직이게 된 기사에 한하여 적용.
    그 기사의 범위안에 있는 함정의 계수 세기.
    
edge case 생각하기. 
i) 중간에 걸리는 경우 
ii) 바깥벽에 부딫히는 경우
iii) 아무일도 안일어날경우 대미지는 없다. 

기사에 대한 정의
r,c,w,h,k => 체력. 
이동함수
밀려난경우 데미지 계산 함수 

map에 대한 정의
(1,1) 이 최상단. 
LxL => 바깥은 2로 감싸기.

기사이동 시 이동이 가능한지 + 모든 기사 이동시키는 함수. 

충돌을 검사하는 방법
1) 모든 기사에 대해 -> 이동했을때. 있는지 확인 => 있다면 충돌한 기사의 다음 확인. 
or 이동했을때 => 그 칸에 있는지 확인 => 넣기(queue) => 다시 다음에 있는지 확인

기사를 => map에 그려둘 것인가 vs 어디에 넣어두고 사용할 것인가. 
넣어두고 사용하기 기사수 30개라 많지 않음
또는 이동후 기사들에 대해서 칸을 일일이 계산해줘야함. 이동한 기사의 범위안에 들어가는지. 
두개의 범위가 겹쳐야한다. => 즉 칸의 이동시 크기를 다 이동시켜야함 => 그냥 r,c 기준으로 범위 check 하기. 


case의 생각. 
그냥 이동할 수도 있음
'''
import collections 
import copy

move_dir = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]


class knight:
    def __init__(self,r,c,w,h,k,k_num):
        self.r = r 
        self.c = c 
        self.w = w
        self.h = h 
        self.k = k
        self.k_num =k_num
    def set_new_p(self,nr,nc):
        
        for r in range(nr,nr+self.h):
            for c in range(nc,nc+self.w):
                if arr[r][c] == 2:
                    #print("col_wall",(r,c))
                    return False
        
        self.r,self.c = nr,nc  
        return True
        
    def check_coll(self, knight):
    # 두 사각형이 겹치지 않는 조건 체크
        if (self.c + self.w < knight.c or 
            knight.c + knight.w < self.c or 
            self.r + self.h < knight.r or 
            knight.r + knight.h < self.r):
            return False
        else:
            return True
    
    def compute_knight_dam(self):
        count = 0 
        for r in range(self.r,self.r+self.h):
            for c in range(self.c,self.c+self.w): 
                if arr[r][c] == 1:
                    count += 1
        self.k -= count
        return self.k 

    def print_state(self):
        print(f"id:{self.k_num}============================================")
        print(f"r: {self.r}, c: {self.c}, h: {self.h}, w: {self.w}, k:{self.k}")
        print(f"=================================================")

def print_knights_state(knights):
    print("*==================================================================*")
    for kn in knights:
        kn.print_state()
    print("*==================================================================*")


def check_can_move(knight,knights,dir_):
    queue=collections.deque()
    main_knight = knight
    
    queue.append(copy.deepcopy(knight)) # copy해서 넣음. 
    
    col_knights=[]
    non_move = False
    while queue:
        cur_knight = queue.popleft()
        
        cur_r = cur_knight.r
        cur_c = cur_knight.c  
    
        
        #문제: 한번 충돌하고 넣음 -> 그 애 연쇄적으로 일어남?
        
        if cur_knight.set_new_p(cur_r+move_dir[dir_][0],cur_c+move_dir[dir_][1]): # 벽에 부딫히는지 확인 후 이동하기. 
            #cur_knight.print_state()
            for kn in knights:
                #kn.print_state()
                if kn.k_num == cur_knight.k_num:
                    continue
                if cur_knight.check_coll(kn):
                    
                    #cur_knight.print_state()
                    #print("=>")
                    #kn.print_state()
                    
                    queue.append(kn)
                    col_knights.append(kn)
        else: # 하나라도벾에 부딫힌 상황 
            
            col_knights.clear()
            non_move=True
            break
    if non_move:
        return knights

    # 이동이 가능한 경우 
    
    
    for kn in knights:
        if kn.k_num == knight.k_num:
            knights.remove(kn)
    
    cur_r = knight.r
    cur_c = knight.c  
    knight.set_new_p(cur_r+move_dir[dir_][0],cur_c+move_dir[dir_][1])
    
    
    
    knights=compute_dem(knights,main_knight.k_num,col_knights)
    knights.append(knight)
        
    
    return knights

def compute_dem(knights,main_n,col_knights):  # 피해를 계산한다.
    global death_knights
    for kn in knights[:]:
        if kn.k_num == main_n or kn not in col_knights:
            continue
        if kn.compute_knight_dam() <=0:
            knights.remove(kn)
            death_knights.append(kn)
    return knights
        
        

L,N,Q = map(int,input().split())
input_arr = [list(map(int,input().split())) for _ in range(L)] 
knight_info =  [list(map(int,input().split())) for _ in range(N)] 
command_info =  [list(map(int,input().split())) for _ in range(Q)] 
all_knights = []
init_knights = []
death_knights = []

knight_hp_set = [0]*N

i = 1
for r,c,h,w,k in knight_info:
    all_knights.append(knight(r,c,w,h,k,i))
    i += 1
init_knights = copy.deepcopy(all_knights)

arr = [[0]*(L+2) for i in range(L+2)]
for i in range(L+2):
    arr[0][i] = 2
    arr[i][0] = 2
    arr[L+1][i] = 2
    arr[i][L+1] = 2
    
for r in range(L):
    for c in range(L):
        arr[r+1][c+1] = input_arr[r][c]

def print_war_arr(arr):
    arr_c = copy.deepcopy(arr)
    for kn in all_knights:
        for r in range(kn.r,kn.r+kn.h):
            for c in range(kn.c,kn.c+kn.w): 
                arr_c[r][c] = kn.k_num+2
    print_arr(arr_c)    


def print_arr(arr):
    print("="*len(arr))
    for row in arr:
        print(*row)
    print("="*len(arr))

#print_arr(arr)
#check_can_move(all_knights[1],copy.deepcopy(all_knights),1)

'''
게임 로직
명령어 순회
check_can_move(명령받는 기사,복사,방향) => all_knight바꾸기.

마지막에 초기 상태와 현재 상태를 비교해서 정답내기 

'''
#print_war_arr(arr)

for com in command_info:
    
    if com[0] not in death_knights:
        for i in range(len(all_knights)):
            kn = all_knights[i]
            if kn.k_num == com[0]:
                move_knight = kn             
                break
        #print(com[1],move_knight.k_num)
        all_knights = check_can_move(move_knight,copy.deepcopy(all_knights),com[1])
    
    #print_knights_state(all_knights)
    #print_war_arr(arr)

ans = 0

for kn in all_knights:
    ans+=(init_knights[kn.k_num-1].k - kn.k)
print(ans)