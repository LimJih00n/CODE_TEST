'''
나무 박멸 25.04.08
제초제를 뿌려 나무의 성장을 억제한다.
벽이 있는 경우 전파되지 않는다.
k의 범위만큼 대각선으로 퍼진다. 

각 턴당
1. 성장 => 주위의 나무 수칸큼 성장
2. 번식 => 주위4칸에 번식. ->
3. 제초가장 많이 없어지는 칸에 뿌린다. 
=> 제초가 일어나면 c년동안 벽이 된다. 


-----
반복을 계속하면 된다
1. 성장. 주위를 보고 값을 1더한다=> 번식전에 일어나면 된다.
2. 주위에 주위가능칸 만큼 내 것을 준다. 
  => 동시에 일어난다. ==> 값이 미리 칸에 반영되면 안된다. 
3. 제초-> 행 -> 열 순으로 탐색하면서 max r,c 찾기. 
제초제 뿌리기 없애기. 

필요한 함수
1. 성장 함수 arr 받아서 성장한 arr 반환
2. 번식함수 arr 받아서 번식한 arr 반환ㅁ
3. 제초 찾기 함수. arr 받아서 가장 많이 없애는 r,c 반환
4. 제초 적용함수 -> 
5. 제초 제거 함수 -> c년후에 사라져야한다. 어떻게 관리할까? => -1로 두고 해가 갈때마다 -는 +1하기. 


제초: -2~
나무: +1
벽: -1 => 문자열로 표현 -> 오류 주의하기.
빈칸: 0

'''

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check_B(r,c,N):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return False

def grow_tree(arr,N):
    
    for r in range(N):
        for c in range(N):
            if arr[r][c]<=0:
                continue
            g_count = 0 
            for sr,sc in zip(dr,dc):
                nr,nc = r+sr,c+sc 
                if check_B(nr,nc,N) and arr[nr][nc] >0:
                    g_count+=1
            arr[r][c] += g_count 
    

def make_tree(arr,N):
    new_arr = [row[:] for row in arr]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c]<=0:
                continue
            g_count = 0 
            n_count = 0
            for sr,sc in zip(dr,dc):
                nr,nc = r+sr,c+sc 
                if check_B(nr,nc,N) and arr[nr][nc] >0:
                    g_count+=1
                if check_B(nr,nc,N) and arr[nr][nc] ==0:
                    n_count+=1
            for sr,sc in zip(dr,dc):
                nr,nc = r+sr,c+sc 
                if check_B(nr,nc,N) and arr[nr][nc]==0:
                    new_arr[nr][nc] += (arr[r][c]//n_count)
    
    
    return new_arr 

def find_max_d_tree(arr,N,K,C): # 대각선으로 쭉 퍼져가야한다.
    move_dig = [
        (1,1),
        (1,-1),
        (-1,1),
        (-1,-1)
    ]
    max_r,max_c = 0,0
    max_de=0
    for r in range(N):
        for c in range(N):
            if arr[r][c] <= 0 or arr[r][c] == -1 :
                continue
            d_count = 0
            d_count += arr[r][c] 
            for move in move_dig:
                cr,cc = r,c  
                
                for k in range(K):
                    nr,nc = cr+move[0],cc+move[1]
                    if not check_B(nr,nc,N):
                        break
                    if  arr[nr][nc] ==0 or arr[nr][nc] == -1:
                        break
                    if arr[nr][nc] >0:
                        d_count += arr[nr][nc] 
                    cr,cc =nr,nc
            if max_de< d_count:
                max_de = d_count 
                max_r,max_c = r,c
    
    return max_r,max_c,max_de  


def kill_the_tree(arr,r,c,N,K,C):
    new_arr = [row[:] for row in arr]
    move_dig = [
        (1,1),
        (1,-1),
        (-1,1),
        (-1,-1)
    ]
    new_arr[r][c] = -C
    for move in move_dig:
        cr,cc = r,c  

        for k in range(K):
            nr,nc = cr+move[0],cc+move[1]
            if not check_B(nr,nc,N):
                break
            if arr[nr][nc] == 0 or arr[nr][nc] == -1:
                new_arr[nr][nc] = -C
                break
            new_arr[nr][nc] = -C
            cr,cc =nr,nc
    return new_arr 

def update_death(arr,N):
    new_arr = [row[:] for row in arr]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == -2:
                new_arr[r][c] = 0
            elif arr[r][c] <= -3:
                new_arr[r][c] +=1
    return new_arr
            
                
    

def init_map(arr):
    new_arr = [row[:] for row in arr]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == -1:
                new_arr[r][c] = -1
    return new_arr


def print_arr(arr,N):
    print("================")
    for r in range(N):
        for c in range(N):
            print(arr[r][c],end=" ")
        print("")
    print("================")
def print_simul(arr,m,N):
    print("====== t:",m,"=========")
    print_arr(arr,N)
    print("=======================")
        

def game_logic(arr,N,M,K,C):
    arr = init_map(arr)
    ans = 0
    C = C+2
    for m in range(M):
        #print("start")
        #print_simul(arr,m,N)
        
        arr = update_death(arr,N)
        grow_tree(arr,N)
        arr = make_tree(arr,N)
        r,c,score= find_max_d_tree(arr,N,K,C)
        
        ans += score 
        
        arr = kill_the_tree(arr,r,c,N,K,C)
        
        #print("end")
        #print_simul(arr,m,N)
    print(ans)
    


N,M,K,C = map(int,input().split())
arr = [list( map(int,input().split())) for i in range(N)]
game_logic(arr,N,M,K,C)
