N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dir_map = {
    "N":(0,1),
    "W":(-1,0),
    "E":(1,0),
    "S":(0,-1)
}
start = [0,0]
time_ = 0
c = False
for dir,dist in zip(dir,dist):
    for i in range(dist):
        start[0] += dir_map[dir][0]
        start[1] += dir_map[dir][1]
        time_ +=1
        if start[0] == 0 and start[1]==0:
            c=True
            break
    if c:
        break
if c:
    print(time_)
else:
    print(-1)