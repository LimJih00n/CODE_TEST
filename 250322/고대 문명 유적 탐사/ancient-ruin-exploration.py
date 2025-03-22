'''
5x5 격자 형태로 유적이되어있고
칸에는 유물조각이 있으며 7종류로 1~7
3x3 만큼 격자를 선택해 회전한다. => 90 180 270 , 시계방향
=> 격자 회전 함수 만들어야함.

회전목표
1) 유물 획득 가치 최대화
->2) 회전 각도 가장 작게
-->3) 회전 중심좌표의 열이 가장 작은 구간 
---->4) 행이 가장 작은 구간 선택.

-> 열->행순으로 탐색하면서 회전하기

유물의 획득
같은 숫자가 3개이상 연결되어있으면 획득 => 유물은 없어짐
없애기 위해서 위치를 알고 있어야한다. 
=> 유적 벽면에 적혀있는 순서대로 새로운 조각이 생김
1) 열번호가 작은 순. 행번호가 큰순.
이미 썻으면 다시 못쓴다. 뒤에꺼 부터 다시 씀

=> 유물이 새로 생성된 다음에도 합쳐지면 합쳐지고 다시 생성해야함

K턴 반복하고. 각 턴마다 가치 총합(없어진거 총합)
미리 끝날 수 있으면 끝나야한다. 

cf: 선택된 격자는 항상 회전해야한다., 유물 1차 획득의 가치를 최대화.

만들어야하는 함수: 
1) 배열 회전 함수 => arr ,r,c, 각도 => 회전된 배열 return 
2) 1차 유물 탐색 함수 (격자 세는 것 만 하기)
3) 유물 획득 함수.
   (격자세는 함수) => 완료
   (조각 바꾸는 함수) =>완료
   (격자세는 함수) => 반복

'''


import collections
import copy

def turn_arr(arr,R,C): # 90도 회전 함수
    new_arr=[]
    '''
    123      741
    456  =>  852
    789      963
    
    row0=>col0
    row1=>col1
    row2=>col2
    
    col0=>rw0
    col1=>rw1
    col2=>rw3
    
    #회전 연습해두기.
    역으로 넣어야한다!!
    
    '''
    col1,col2,col3=[],[],[]
    
    for r in range(R-1,R+2): 
        
        col1.append(arr[r][C-1])
        col2.append(arr[r][C])
        col3.append(arr[r][C+1])
    
    new_arr=[col1[::-1],col2[::-1],col3[::-1]]
    
    for r in range(3):
        for c in range(3):
            arr[r+R-1][c+C-1] = new_arr[r][c]
    
    
    
    return arr   

def check_b(r,c):
    if r>=0 and c>=0 and r<5 and c<5:
        return True
    return False

# compute_tresure의 경우 한 경로를 모두 봐야함 이런 경우는 dfs가 더 유리함함

def compute_tresure(arr): # 모든 map 탐색. 
    tem_count=0
    tot_count = 0
    queue = collections.deque()
    visted = [[False]*5 for i in range(5)]
    # 얼마나 같은 수로 연속하고 있는지 넣기기
    
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    
    
    
    def dfs(r,c,value,path):
        if not check_b(r,c) or visted[r][c] or value != arr[r][c]:
            return
        visted[r][c] = True
        
        path.append((r,c))
        for sr,sc in zip(dr,dc):
            dfs(r+sr,c+sc,value,path)


    trea_region = []

    for i in range(5):
        for j in range(5):
            if not visted[i][j]:
                
                path=[]
                dfs(i,j,arr[i][j],path)
                if len(path)>=3:
                    trea_region += path
                    tot_count += len(path)
    return tot_count,trea_region
                
    
    
        
        


def print_arr(arr):
    print("==========")
    for row in arr:
        print(*row)
        
        
K,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(5)]
sub_tre = list(map(int,input().split()))
sub_tre_idx = 0
#print_arr(arr)
#turn_arr(arr,2,2)
tot_tre_count,tot_tre_path=compute_tresure(arr)
tot_tre_path = sorted(tot_tre_path,key = lambda x:(x[1],-x[0]))



while True:
    ans = 0
    if K == 0:
        break
    max_pos = (1,1)
    max_count=0
    cur_turn = 4
    # find degree and r,c
    for c in range(1,4):
        for r in range(1,4):
            temp_arr = copy.deepcopy(arr)
            temp_arr = turn_arr(temp_arr,r,c)
            tot_tre_count,tot_tre_path=compute_tresure(temp_arr)
            if max_count <= tot_tre_count:
                
                
                if max_count<tot_tre_count:
                    max_count=tot_tre_count
                    max_pos=(r,c)
                    cur_turn=1
                if max_count==tot_tre_count and cur_turn>1:
                    max_pos=(r,c)
                    cur_turn=1
                
            temp_arr = turn_arr(temp_arr,r,c)
            tot_tre_count,tot_tre_path=compute_tresure(temp_arr)
            if max_count <= tot_tre_count:
                
                if max_count<tot_tre_count:
                    max_count=tot_tre_count
                    max_pos=(r,c)
                    cur_turn=2
                if max_count==tot_tre_count and cur_turn>2:
                    max_pos=(r,c)
                    cur_turn=2
            temp_arr = turn_arr(temp_arr,r,c)
            tot_tre_count,tot_tre_path=compute_tresure(temp_arr)
            if max_count <= tot_tre_count:
                
                if max_count<tot_tre_count:
                    max_count=tot_tre_count
                    max_pos=(r,c)
                    cur_turn=3
                if max_count==tot_tre_count and cur_turn>3:
                    max_pos=(r,c)
                    cur_turn=3
                    
                    cur_turn=3
    
    if cur_turn==4:
        continue


    for i in range(cur_turn):
        arr = turn_arr(arr,max_pos[0],max_pos[1])
    
    turn_tree_count = 0
    tot_tre_count,tot_tre_path=compute_tresure(arr)
    tot_tre_path = sorted(tot_tre_path,key = lambda x:(x[1],-x[0]))
    
    while tot_tre_count!=0:
        #print_arr(arr)
        #print(tot_tre_path)
        ans += tot_tre_count
        for pos in tot_tre_path:
            #print(sub_tre_idx,sub_tre[sub_tre_idx])
            arr[pos[0]][pos[1]] = sub_tre[sub_tre_idx]
            sub_tre_idx+=1
        #print_arr(arr)
        tot_tre_count,tot_tre_path=compute_tresure(arr)
        tot_tre_path = sorted(tot_tre_path,key = lambda x:(x[1],-x[0]))
    K-=1
    if ans==0:
        break
    print(ans,end=" ")
    
        
            
            

'''
game logic
1) r,c에서 회전 범위 주의
2) 개수 확인 => 최대인 r,c 찾기
3) 연속된거 세기 -> 바꾸기 -> 연속된거 세기 -> 바꾸기. re가 0일때까지 반복.
위치 가르키는 거 있어야함.
'''





    
    
    