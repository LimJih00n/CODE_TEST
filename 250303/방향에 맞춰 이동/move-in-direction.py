N = int(input())
command = [ input().split() for i in range(N)]
dir_dic = {
    "W":(-1,0),
    "E":(1,0),
    "N":(0,1),
    "S":(0,-1)
}
start = [0,0]
for c,v in command:
    start[0] += dir_dic[c][0] *int(v)
    start[1] += dir_dic[c][1] *int(v)
print(*start)