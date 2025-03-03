commands = input()

# Please write your code here.
dir_ = 0
dir_move = [(0,1),(1,0),(0,-1),(-1,0)]
start_po = [0,0]
spend_time = 0
check_ans = False
for c in commands:
    if c =="F":
        start_po[0] +=dir_move[dir_][0]
        start_po[1] +=dir_move[dir_][1]
    if c == "L":
        dir_ = dir_ +1 if dir_ <3 else 0
    if c=="R":
        dir_ = dir_-1 if dir_ >0 else 3
    spend_time +=1
    if start_po[0] ==0 and start_po[1]==0:
        check_ans = True
        break
if check_ans:
    print(spend_time)
else:
    print(-1)
    