'''
for문 순회에서 복사 주의하기
복제안하고 탐색할경우 씹어지는 경우가 발생한다. 탐색은 복사본으로하고
그 친구 삭제는 원본으로 할 수 있게하기.

NxM 격자
포탑 준재. 공격력. 0이되면 부서짐. 부서진 포탑 존재가능

1턴이란
4가지 진행 K번 반복
부서지지 않은 포탑이 1개가 된다면 그 즉시 중지=> 포탑 1개 남으면 중지 

1. 공격자 선정
unbroken 중 가장 약한 포탑이 공격자 선정
이 공격자는 N+M 만큼 공격력 증가 

가장 약한 포탑 선전 기준
1. 공격력이 가장 낮은 => 저장
2. 1이 2개이상이면 "가장 최근에 공격한 포탑" => 저장
3. 2개 이상이면 "행,열 합이 가장 큰 포탑" => 저장
4. 열값이 가장 큰 포탑 => 가장 오른쪽

2. 공격
가장 강한 포탑 공격
1. 가장 공격력이 높은 포탑
2. 공격한지 가장 오래된 포탑
3. 행열합이 가장 작은 포탑
4. 열이 가장 작은 포탑

1) 레이저 공격 => 상하좌우 4개 방향. 보서진 포탑이 벽. 
=> 밖으로 나가면 반대편으로 돌아옴.
길이 똑같은 경로 2개 이상 => 우하좌상 순
경로 선택  후 공격. 공격대상은 공격력만큼.=>받은 만큼 공격력 줄어듬
경로에 있는 포탑도 공격받음. 절판만큼
or 
2) 포탄 공격 => 경로가 없는 경우
대상은 공격력만큼. 아닌 대상은 8방으로 절반 피해. 공격자는 영향 x
가장자리에 떨어질시 "반대편 격자도 영향" 미침

3. 포탑 부서짐 -> 0이하는 부서짐

4. 포탑 정비 => 공격자도 아니고 피해를 입지 않은 포탑은 공격력+1


cf: 반대편으로 넘어오는 경우를 생각하야한다. bound되는 경우 좌표 돌려주기. 
필요함수:
포탑 선정 함수 => 포탑은 다양한 정보를 가지고 있어야한다

포탑: 
- r,c, 발사 턴, 공격력.

1) 약자
2) 강자
3) 레이저 발사 함수
레이저 이동함수 => 경로 반환 => 좌표

4) 포탄 발사함수 => 영향 반환 => 좌표표
=> 범위 계산

피해계산 함수 => 레이저 or 포탄에 대해 피해 계산하기. 

5) 피해 없는 포탑 증강 함수. 

만들 것
1. 포탑 정의의
2. 약자 탐색
3. 강자 탐색

로직을 어떻게 할 것인지
포탑 class를 만들고 포탑들을 넣어둔다. 
살아남은 포탑과 죽은 포탑을 분리한다.
죽은 포탑은 죽은 포탑 리스트에 넣어둔다. => 이동시 반영해야한다. 
턴 진행한다. 

map 탐색시 어떻게 할 것인가? 
사방 탐색 => 죽은 포탑있으면 못감&방문했으면 못감. 

리스트에 넣어서 기본적으로 관리. 삭제 복제 생성 주의하기.

확인해야할 것
1) 경로 없을때 포탄 쏘는지
2) 레이저의 경로, 포탄의 경로 잘 구하는지. 
    어떻게 확인??


임의로 그리는 함수 만들기

아니면 튜플로 두고. 해당 기준에 맞취서 정렬해서 사용하기.
튜플: r,c, 공격력, 턴, 행열합, 열
            2     3     4     5
=> 잘 선정하는지 확인해야함 => 모두 오름차순 정렬후, 가장 앞값. 가장 작은 갚 쓰기 

기능 단위 test
'''
import copy 
import collections


def print_arr(arr):
    print("="*len(arr))
    for row in arr:
        print(*row)

def print_simul_path(arr,path):
    p_arr= [[0]*M for i in range(N)]
    for po in path:
        p_arr[po[0]][po[1]] = 1
    print("======path_simul======")
    print_arr(p_arr)
    
def print_now_tarret(tarrets):
    p_arr = [[0]*M for i in range(N) ]
    print("======tarret_simul======")
    for po in tarrets:
        p_arr[po[0]][po[1]] = po[2]
    
    print_arr(p_arr)
    
    return p_arr
    

def check_over_flow(r,c):
    nr,nc= r,c
    if r>=N:
        nr=0 
    if c>=M:
        nc = 0 
    if r<0:
        nr = N-1
    if c<0:
        nc = M-1
    return nr,nc
    
#문제: 바로 raser가 가능 경우우
def make_raser_path(attacker,depender):
    visted = set()
    queue = collections.deque()
    
    attacker_node = (attacker[0],attacker[1])
    depender_node = (depender[0],depender[1])
    
    queue.append((attacker_node,[]))
    visted.add(attacker_node)
    
    move_dir = [
        (0,1),
        (1,0),
        (0,-1),
        (-1,0)
    ]
    re_len = M*N 
    re =[]
    find_path = False
    while queue:
        cur_node,path_ = queue.popleft()
        
        for move in move_dir:
            nr,nc = cur_node[0]+move[0] , cur_node[1]+move[1]
            nr,nc = check_over_flow(nr,nc)
            if (nr,nc) not in tarrets_death_po and (nr,nc) not in visted:
                if (nr,nc) == depender_node:
                    if re_len > len(path_):
                        re_len = len(path_)
                        re = path_
                        find_path = True
                        
                else:
                    path_.append((nr,nc))
                    queue.append(((nr,nc),path_[:]))
                    visted.add((nr,nc))
                    path_.pop()
                    
                
    
    return find_path,re 
    

                
            
def make_boom_path(attacker,depender):
    #상하좌우 
    move_dir = [
        (1,0),
        (0,1),
        (-1,0),
        (0,-1),
        (1,1),
        (-1,1),
        (-1,-1),
        (1,-1),
        
    ]
    cur_node = (depender[0],depender[1])
    path_ = []
    for move in move_dir:
        nr,nc = cur_node[0]+move[0],cur_node[1]+move[1]
        nr,nc = check_over_flow(nr,nc)
        if (nr,nc) != (attacker[0],attacker[1]) and (nr,nc) not in tarrets_death_po:
            path_.append((nr,nc))
    return path_

def check_compute_tarret(tarrets,tarrets_live_po,tarrets_death_po):
    
    
    
    for t in tarrets[:]:
        
        if t[2]<=0:
            tarrets_live_po.remove((t[0],t[1]))
            tarrets.remove(t)
            tarrets_death_po.append((t[0],t[1]))
    return tarrets,tarrets_live_po,tarrets_death_po

def compute_dem(attacker,depender,path,tarrets):
    depender[2] -= attacker[2]
    
    attacker_node = (attacker[0],attacker[1])
    depender_node = (depender[0],depender[1])
    
    revise_tarrets = []
    
    for po in path:
        
        for t in range(len(tarrets)):
            node = (tarrets[t][0],tarrets[t][1])
            if po==node:
                tarrets[t][2] -= attacker[2]//2
                
            else: 
                
                if (node not in path) and (node != attacker_node) and (node != depender_node) and (tarrets[t] not in revise_tarrets):
                    revise_tarrets.append(tarrets[t])
    if len(path)==0:
        for t in range(len(tarrets)):
            node = (tarrets[t][0],tarrets[t][1])
            
            if (node not in path) and (node != attacker_node) and (node != depender_node) and (tarrets[t] not in revise_tarrets):
                revise_tarrets.append(tarrets[t])
        
    
    
    return tarrets,revise_tarrets

tarrets = [] # 모든 정보, 
tarrets_live_po = [] # 좌표값만 저장. 산애 
tarrets_death_po = [] #좌표값만 저장. 죽은애

N,M,K = map(int,input().split())



arr = [list(map(int,input().split())) for i in range(N)]


'''
raser로 옆에 있는 거 때릴경우 path가 안나옴 근데 이럴경우에는 데미지는 들어가나
revise를 제대로 못해줌. 왜냐하면 path를 확인하면서 보기때문
즉 모든 경우에 대해 path가 있을 것이라 생각한 것은 패착.
'''

for r in range(N):
    for c in range(M):
        if arr[r][c] >0:
            tarrets.append([r,c,arr[r][c],0,r+c,c])
            tarrets_live_po.append((r,c))
        else:
            tarrets_death_po.append((r,c))



        
        

        
def game_logic(tarrets,tarrets_live_po,tarrets_death_po,K):
    
    
    tarrets,tarrets_live_po,tarrets_death_po = check_compute_tarret(tarrets,tarrets_live_po,tarrets_death_po)
    
    for k in range(1,K+1):
        #print("===============================",k)
        revise_tarrets=[]
        tarrets = sorted(tarrets, key = lambda x:(x[2],-x[3],-x[4],-x[5]))
        #print("ff",tarrets)
        attacker = tarrets[0]
        
        depender = tarrets[-1]
        attacker[2] += (M+N)
        attacker[3] = k 
        
        
        
        
        find_path,attack_path = make_raser_path(tarrets[0],tarrets[-1])
        if not find_path: # 없다고 인식해버림 => 이런 거 주의. 길이가 즉 바로 가는 경우에 대해서도 생각해야한다.
            #print("boom!")
            attack_path = make_boom_path(tarrets[0],tarrets[-1])
        
        #print_simul_path(arr,attack_path)
        
        
        tarrets,revise_tarrets = compute_dem(attacker,depender,attack_path,tarrets)
        #print_now_tarret(tarrets)
        #print("c",tarrets)
        tarrets,tarrets_live_po,tarrets_death_po = check_compute_tarret(tarrets,tarrets_live_po,tarrets_death_po)
        #print("c2",tarrets)
        if len(tarrets)==1:
            
            break
        for t in revise_tarrets:
            t[2] +=1
            
        #print_now_tarret(tarrets)
    #ans 자체를 잘못 생각함
    #arr로 보면 저게 맞을지 몰라도 나는 point로 보고 있었음.... row가 아님 => 결과 항상 잘 나오는지check하기.    
    #로직 완전 의심하면서 check하기
    #print_now_tarret(tarrets)
    ans = 0
    for t in tarrets:
        ans = max(ans,t[2])
    
    return ans
        
        
print(game_logic(tarrets,tarrets_live_po,tarrets_death_po,K))