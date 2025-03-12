import copy
N,M,X,Y,K = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)] 
commands = list(map(int,input().split()))

move_dir = [
    (0,0),
    (0,1),
    (0,-1),
    (-1,0),
    (1,0)
]



dic_cur_po = (X,Y)
DICE = {
    "U" : 0, "D" : 0, "S" : 0, 
    "N" : 0, "E" : 0, "W" : 0,
}
def dice_role(dir_command):
    temp_dice = copy.deepcopy(DICE)
    if dir_command == 1:
        DICE["W"] = temp_dice["U"]
        DICE["U"] = temp_dice["E"]
        DICE["E"] = temp_dice["D"]
        DICE["D"] = temp_dice["W"]
    if dir_command == 2:
        DICE["W"] = temp_dice["D"]
        DICE["U"] = temp_dice["W"]
        DICE["E"] = temp_dice["U"]
        DICE["D"] = temp_dice["E"]
    if dir_command == 3:
        DICE["N"] = temp_dice["D"]
        DICE["U"] = temp_dice["N"]
        DICE["S"] = temp_dice["U"]
        DICE["D"] = temp_dice["S"]
    if dir_command == 4:
        DICE["N"] = temp_dice["U"]
        DICE["U"] = temp_dice["S"]
        DICE["S"] = temp_dice["D"]
        DICE["D"] = temp_dice["N"]

r,c = X,Y
for command in commands:
    
    nr,nc = r+move_dir[command][0],c+move_dir[command][1]
    if nr<0 or nc<0 or nc>=M or nr>=N:
        continue
    r,c = nr,nc
    dice_role(command)
    if arr[r][c] == 0:
        arr[r][c] = DICE["D"]
    else:
        DICE["D"]=arr[r][c]
        arr[r][c] = 0
    print(DICE["U"])
        