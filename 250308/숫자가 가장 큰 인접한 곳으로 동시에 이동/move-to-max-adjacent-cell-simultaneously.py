n, m, t = map(int, input().split())

# Create n x n grid
arr = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]
marbles = [(r1,c1) for r1,c1 in zip(r,c) ]

# Please write your code here.
'''
what? 구슬 움직임 => 상하좌우를 기준으로 높은 칸으로 이동. 이동 우선순위 따름
"그냥 큰게 아니라 가장 큰 값임"
이동 후 충돌 시 구슬은 사라짐 T초 후 남아있는 구슬의 수를 구하기. 
문제 잘보기 "가장큰"
how?
1.구슬일 경우 이동시키기.
2.이동 나타내는 배열 만들고. 겹치면 초기화
1,2반복
'''
import copy
def check_b(r,c):
    if r>=0 and c>=0 and r<n and c<n:
        return True
    return False
move_dir = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
]
m_map = [[0] * n for i in range(n)]
for r,c in zip(r,c):
    m_map[r][c] = 1
# m_map 초기화
ans = 0

while True:
    can_move=[]
    remove_mable = []
    for marble in marbles:
        mr,mc = marble
        max_v,move_p = arr[mr][mc],(mr,mc)
        for i in range(4):
        
        
            n_mr = (mr)+move_dir[i][0]
            n_mc = (mc)+move_dir[i][1]
            
            if check_b(n_mr,n_mc) and arr[n_mr][n_mc] > max_v:
                
                max_v = arr[n_mr][n_mc]
                move_p = (n_mr,n_mc)

        if move_p in can_move:
            can_move.remove(move_p)
            remove_mable.append(move_p)
        elif  move_p not in remove_mable: #문제 같은 게 또 들어오면 오류 나옴 - 3개가 겹칠 수 있음
            can_move.append(move_p)
        
            
                
    marbles = copy.deepcopy(can_move)
    t -= 1
    
    if t==0:
        ans = len(can_move)
        break

print(ans)

