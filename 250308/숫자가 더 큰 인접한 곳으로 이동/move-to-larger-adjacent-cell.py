n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
'''
what?
r,c에서 시작해 최대값을 찾아가는 과정 
이동가능 중 더 큰 위치를 찾아갈때까지 의 경로를 그림
how?
4방 이동 max인 곳 저장. 상하좌우에서 이동임.
순회하면서 큰값의 위치 찾기. idx 넣어두기. 가장 작은 idx로 이동하기
path 넣기 
이동 없어지는 순간 끝
'''
r,c = r-1,c-1
move_dir = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
]
path = []
def check_b(r,c):
    if r>=0 and c>=0 and r<n and c<n:
        return True
    return False
while True:
    can_go=[]
    path.append(arr[r][c])
    for i in range(4):
        nr,nc = r+move_dir[i][0],c+move_dir[i][1]
        if check_b(nr,nc) and arr[nr][nc] > arr[r][c]:
            can_go.append(i)
    if len(can_go) == 0:
        break
    else:
        r,c = r+move_dir[can_go[0]][0],c+move_dir[can_go[0]][1]
print(*path)
        
