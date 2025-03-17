'''
1이상 4이하의 정수로만 되어있음
=> gen_h

아름다운 수 조건. 
연속해서 1333221 나와야함. 
연속된 개수 세기. 실제나온 수 세기. => 
22212 =>x 

연속 3번
나온수 4번 
2번 나오고 count + 1
count = 나온수 // n
'''

N = int(input())
arr = [i for i in range(1,5)]

def gen_h(ele,r):
    re = []

    def dfs(path):
        if len(path) == r:
            re.append(path[:])
            return
        for i in range(len(ele)):
            path.append(ele[i])
            dfs(path)
            path.pop()
    dfs([])
    return re

# 22122 => 4 2
# 22212  => 4 1

def check_beauty_num(li):
    
    check_arr = [ [0]*5 for i in range(3) ]
    # check_arr[i][0] => count
    # check_arr[i][1] => 연속 count 구간
    # check_arr[i][2] => 얼마나 연속하고 있는지 count 
    consis_num = 0
    if len(case_ ) == 0:
        return False
    consis_num=li[0]
    check_arr[0][consis_num]+=1

    for i in range(1,len(li)):
        check_arr[0][li[i]] += 1
        if li[i-1] == li[i]: #연속하는 경우 
            consis_num = li[i]
            check_arr[2][li[i]] += 1
            if (check_arr[2][li[i]]+1) % li[i] == 0:
                check_arr[1][li[i]] += 1
        else: # 연속안하는 경우  
            
            check_arr[2][consis_num] = 0
            consis_num = 0

    check = False
    con = check_arr[0][2] == check_arr[1][2] * 2 and check_arr[0][3] == check_arr[1][3] * 3 and check_arr[0][4] == check_arr[1][4] * 4
    return con

cases = gen_h(arr,N)

if N == 1:
    print(1)
else:
    ans = 0
    for case_ in cases:
        if check_beauty_num(case_):
            ans+=1
    print(ans)





            
