import copy

def gen_h(elements,r):
    re = []

    def dfs(path):

        if len(path) == r:
            re.append(path[:])
            return re
        for i in range(len(elements)):
            path.append(elements[i])
            dfs(path)
            path.pop()
    dfs([])
    return re
#"U" "D" "L" "R"
def print_ARR(arr):
    print("===========")
    for row in arr:
        print(*row)
    print("=============")
    
def move_func(arr,dirc):
    check_merge = []
    if dirc=="U":#r-1이 다음칸 
        
        for c_ in range(n):
            for r_ in range(1,n):
                if arr[r_][c_]==0:
                    continue
                r,c = r_,c_
                while True:
                    nr,nc = r-1,c
                    if nr >=n or nc >= n or nr<0 or nc<0:
                        break
                    if arr[r][c] == arr[nr][nc] and (nr,nc) not in check_merge: 
                        #합칠 수 있는 경우 
                        arr[nr][nc] = arr[r][c] * 2 
                        arr[r][c] = 0
                        check_merge.append((nr,nc))
                        break
                    
                    elif arr[nr][nc]==0: 
                        arr[nr][nc],arr[r][c] = arr[r][c],arr[nr][nc]
                        r -= 1
                    else:#수가 이미 있는 경우 
                        break
    if dirc == "D": #r+1이 다음 칸 
        
        for c_ in range(n):
            for r_ in range(n-2,-1,-1):
                if arr[r_][c_]==0:
                    continue
                r,c = r_,c_
                while True:
                    nr,nc = r+1,c
                    if nr >=n or nc >= n or nr<0 or nc<0:
                        break 
                    
                    if arr[r][c] == arr[nr][nc] and (nr,nc) not in check_merge: 
                        #합칠 수 있는 경우 
                        arr[nr][nc] = arr[r][c] * 2 
                        arr[r][c] = 0
                        check_merge.append((nr,nc))
                        break
                    
                    elif arr[nr][nc]==0: 
                        arr[nr][nc],arr[r][c] = arr[r][c],arr[nr][nc]
                        r += 1
                    else:#수가 이미 있는 경우 
                        break
    if dirc == "L": #c-1이 다음 칸 
        for r_ in range(n):
            for c_ in range(1,n):
                if arr[r_][c_]==0:
                    continue
                r,c = r_,c_
                while True:
                    nr,nc = r,c-1
                    if nr >=n or nc >= n or nr<0 or nc<0:
                        break
                    if arr[r][c] == arr[nr][nc] and (nr,nc) not in check_merge: 
                        #합칠 수 있는 경우 
                        arr[nr][nc] = arr[r][c] * 2 
                        arr[r][c] = 0
                        check_merge.append((nr,nc))
                        break
                 
                    elif arr[nr][nc]==0: 
                        arr[nr][nc],arr[r][c] = arr[r][c],arr[nr][nc]
                        c -= 1
                    else:#수가 이미 있는 경우 
                        break
    if dirc == "R": #c+1이 다음 칸 
        for r_ in range(n):
            for c_ in range(n-2,-1,-1):
                
                if arr[r_][c_]==0:
                    continue
                
                r,c = r_,c_
                while True:
                    
                    nr,nc = r,c+1
                    if nr >=n or nc >= n or nr<0 or nc<0:
                        break
                    if arr[r][c] == arr[nr][nc] and (nr,nc) not in check_merge : 
                        #합칠 수 있는 경우 
                        arr[nr][nc] = arr[r][c] * 2 
                        arr[r][c] = 0
                        check_merge.append((nr,nc))
                        break
                    elif arr[nr][nc]==0:#수가 이미 있는 경우 
                        arr[nr][nc],arr[r][c] = arr[r][c],arr[nr][nc]
                        c += 1
                    else:
                        break
                        
    
    
    return arr 

n = int(input())
ARR = [list(map(int,input().split())) for i in range(n)]



ans = 0
cases = gen_h(["U","D","L","R"],5)

for move_case in cases:
    case_map = copy.deepcopy(ARR)
    
    for move in move_case:
        
        case_map = move_func(case_map,move)
        
    ans = max(ans,max([max(row) for row in case_map]))
print(ans)
