import collections




def check_bound(r,c):
    if r>=0 and c>=0 and r<N and c<N:
        return True
    return False

def compute_res_pos(po1,po2):

    dr,dc = po1[0]-po2[0],po1[1]-po2[1]

    if dr<0 and dc == 0:
        return "U"
    elif dr<0 and dc>0:
        return "UR"
    elif dr==0 and dc>0:
        return "R"
    elif dr>0 and dc>0:
        return "DR"
    elif dr>0 and dc==0:
        return "D"
    elif dr>0 and dc<0:
        return "DL"
    elif dr==0 and dc<0:
        return "L"
    elif dr<0 and dc<0:
        return "UL"


def medusa_seem(po, dir_): # 현재 위치와 방향을 받는다. 
    seem_dic = {
        "U":[(-1,0),(-1,-1),(-1,1)],
        "D":[(1,0),(1,-1),(1,1)],
        "L":[(0,-1),(-1,-1),(1,-1)],
        "R":[(0,1),(-1,1),(1,1)]
    }
    seem_array = []
    seem_queue = collections.deque()
    stone_war_set = []
    not_stone_war = []

    for ele in seem_dic[dir_]:
        nr,nc = po[0]+ele[0],po[1]+ele[1]
        if check_bound(nr,nc) and (nr,nc) not in seem_array:
            seem_queue.append((nr,nc))
            seem_array.append((nr,nc))
        if (nr,nc) in war_po_set:
            war_dir = compute_res_pos((nr,nc),po)
            
            if (nr,nc,war_dir) not in stone_war_set:
                for _ in range(war_po_set.count((nr,nc))):
                    stone_war_set.append((nr,nc,war_dir))
    
    while seem_queue:
        cur_po = seem_queue.popleft()
        for ele in seem_dic[dir_]:
            nr,nc = cur_po[0]+ele[0],cur_po[1]+ele[1]
            if check_bound(nr,nc) and (nr,nc) not in seem_array:
                seem_queue.append((nr,nc))
                seem_array.append((nr,nc))
            if (nr,nc) in war_po_set:
                war_dir = compute_res_pos((nr,nc),po)
                            
                if (nr,nc,war_dir) not in stone_war_set:
                    for _ in range(war_po_set.count((nr,nc))):
                        
                        stone_war_set.append((nr,nc,war_dir))
    
    return seem_array,stone_war_set

def block_war(stone_war_set,medusa_seem_array): # 시야에서 없는 거지 실제로 없는 것은 아니다. 
    war_seem_dic={
        "U":[(-1,0)],
        "UR":[(-1,0),(-1,1)],
        "R":[(0,1)],
        "DR":[(1,0),(1,1)],
        "D":[(1,0)],
        "DL":[(1,0),(1,-1)],
        "L":[(0,-1)],
        "UL":[(-1,-1),(-1,0)],
    }
    seem_array = []
    seem_queue = collections.deque()
    non_stone_war =[]

    for war in stone_war_set:
        cur_r,cur_c,dir_ = war 
        if (cur_r,cur_c) in non_stone_war:
            continue

        for ele in war_seem_dic[dir_]:
            nr,nc = cur_r+ele[0],cur_c+ele[1]
            if check_bound(nr,nc) and (nr,nc) not in seem_array:
                seem_queue.append((nr,nc))
                seem_array.append((nr,nc))
                if (nr,nc) in medusa_seem_array:
                    medusa_seem_array.remove((nr,nc))
            if (nr,nc) not in non_stone_war and (nr,nc) in war_po_set:
                    non_stone_war.append((nr,nc))
        
        while seem_queue:
            cur_po = seem_queue.popleft()
            for ele in war_seem_dic[dir_]:
                nr,nc = cur_po[0]+ele[0],cur_po[1]+ele[1]
                if check_bound(nr,nc) and (nr,nc) not in seem_array:
                    seem_queue.append((nr,nc))
                    seem_array.append((nr,nc))
                    if (nr,nc) in medusa_seem_array:
                        medusa_seem_array.remove((nr,nc))
                
                if (nr,nc) not in non_stone_war and (nr,nc) in war_po_set:
                    non_stone_war.append((nr,nc))
                    
    return medusa_seem_array,non_stone_war

def make_path(start_node):
    
    queue = collections.deque()
    
    queue.append((start_node,[]))
    visted = [[False] * N for i in range(N)]
    
    move_dir = {
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    }
    
    re = []
    
    while queue:
        cur_node,path = queue.popleft()
        
        for move in move_dir:
            next_r,next_c = cur_node[0]+move[0],cur_node[1]+move[1]
            if check_bound(next_r,next_c) and arr[next_r][next_c] == 0 and not visted[next_r][next_c]:
                path.append(move)
                
                if next_r == er and next_c == ec:
                    path.pop()
                    return path[:]
                
                queue.append(((next_r,next_c),path[:]))
                path.pop()
                visted[next_r][next_c] = True
    return -1
            
def move_1(medusa_po,war_po): # 다음좌표 반환환
    move_dir = [
        (-1,0),
        (1,0),
        (0,-1),
        (0,1)
    ]
    cur_dist = abs(medusa_po[0]-war_po[0]) + abs(medusa_po[1]-war_po[1])
    for move in move_dir:
        nr,nc = war_po[0]+move[0],war_po[1]+move[1]
        next_dist = abs(medusa_po[0]-nr) + abs(medusa_po[1]-nc)
        if check_bound(nr,nc) and (nr,nc) not in medusa_seem_array and next_dist<cur_dist:
            return (nr,nc)
    return war_po
def move_2(medusa_po,war_po):
    move_dir = [
        (0,-1),
        (0,1),
        (-1,0),
        (1,0),
    ]
    cur_dist = abs(medusa_po[0]-war_po[0]) + abs(medusa_po[1]-war_po[1])
    for move in move_dir:
        nr,nc = war_po[0]+move[0],war_po[1]+move[1]
        next_dist = abs(medusa_po[0]-nr) + abs(medusa_po[1]-nc)
        
        if check_bound(nr,nc) and (nr,nc) not in medusa_seem_array and next_dist<cur_dist:
            return (nr,nc)
    return war_po
    
    


N,M = map(int,input().split())
sr,sc,er,ec = map(int,input().split())
war_po_set = list(map(int,input().split()))
war_po_set = [(war_po_set[i],war_po_set[i+1]) for i in range(0,len(war_po_set),2)]

arr = [list(map(int,input().split())) for i in range(N)]


'''
arr = [[0]*N for _ in range(N)]
arr[sr][sc]=3

for po in war_po_set:
    arr[po[0]][po[1]] = 2

seem_array,stone_war_set = medusa_seem((sr,sc),"L")
print(seem_array,stone_war_set)
real_non_stone_war = []
for po in war_po_set:
    if not po in seem_array:
        real_non_stone_war.append((po))
medusa_seem_array,non_stone_war = block_war(stone_war_set,seem_array)
print(non_stone_war)



real_non_stone_war += non_stone_war
print(real_non_stone_war)




for row in arr:
    print(*row)
'''



medusa_path = make_path((sr,sc))

#print(medusa_path)
if medusa_path == -1:
    print(-1)
else:
    r,c=sr,sc 
    for move in medusa_path:
        move_dis_sum,stone_war_sum, attack_war = 0,0,0
        next_war_set = []
        nr,nc = r+move[0],c+move[1]
        min_stone_war = len(war_po_set)
        n_seen_dir = "U"
        stone_war = []
        
        for seen_dir in ["U","D","L","R"]:
            seem_array,stone_war_set = medusa_seem((nr,nc),seen_dir)
            real_non_stone_war = []
            for po in war_po_set:
                if not po in seem_array:
                    real_non_stone_war.append((po))
            
            medusa_seem_array,non_stone_war = block_war(stone_war_set,seem_array)
            real_non_stone_war += non_stone_war
        
        
            
            if min_stone_war > len(real_non_stone_war):
                min_stone_war = len(real_non_stone_war)
                n_seen_dir = seen_dir
        
        
        seem_array,stone_war_set = medusa_seem((nr,nc),n_seen_dir)
        real_non_stone_war = []
        for po in war_po_set:
            if not po in seem_array:
                real_non_stone_war.append((po))
        medusa_seem_array,non_stone_war = block_war(stone_war_set,seem_array)
        real_non_stone_war += non_stone_war
        
        #print(n_seen_dir)
        #print(medusa_seem_array)
        #print(war_po_set,real_non_stone_war)
        
        for war_po in war_po_set:
            
            if war_po == (nr,nc):
                continue
            
            if war_po in real_non_stone_war:
                before_po = war_po
                
                
                
                w_po = move_1((nr,nc),war_po)
                #print("step1",before_po,w_po,(nr,nc))
                if w_po!=before_po:
                    move_dis_sum+=1
                if w_po == (nr,nc):
                    attack_war+=1
                    continue
                before_po = w_po
                w_po = move_2((nr,nc),w_po)
                #print("step2",before_po,w_po,(nr,nc))
                if w_po!=before_po:
                    move_dis_sum+=1
                
                if w_po == (nr,nc):
                    attack_war+=1
                    continue
                else:
                    next_war_set.append(w_po)
                
            else:
                stone_war_sum+=1
                next_war_set.append(war_po)
        war_po_set = next_war_set
        
        r,c = nr,nc
        print(move_dis_sum,stone_war_sum, attack_war)
    print(0)
