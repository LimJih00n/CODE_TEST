
#
head_dir = 0
           #  N    E      S     W
move_dir = [(0,1),(1,0),(0,-1),(-1,0)]
command = list(input())

start = [0,0]
for c in command:
    if c == "L":
        head_dir = head_dir-1 if head_dir>0 else 3
    elif c=="R":
        head_dir = head_dir+1 if head_dir>2 else 0
    else:
        start[0] += move_dir[head_dir][0]
        start[1] += move_dir[head_dir][1]
print(*start)