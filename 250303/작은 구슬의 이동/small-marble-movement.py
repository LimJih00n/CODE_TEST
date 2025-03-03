n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
def check_b(r,c,dir_):
    if r==0 or c==0 or r>n or c>n:
        if dir_=="U":
            return "D"
        if dir_=="D":
            return "U"
        if dir_=="R":
            return "L"
        if dir_=="L":
            return "R"
    else:
        return "G"
dir_map={
    "U":(-1,0),
    "D":(1,0),
    "R":(0,1),
    "L":(0,-1)
}
start = [r,c]
cur_dir = d
while True:
    result = check_b(start[0],start[1],cur_dir)
    if result =="G":
        start[0] += dir_map[cur_dir][0]
        start[1] += dir_map[cur_dir][1]
    else:
        cur_dir = result
        start[0] += dir_map[cur_dir][0]
        start[1] += dir_map[cur_dir][1]
        
    t -= 1
    if t==-1:
        break
print(*start)


