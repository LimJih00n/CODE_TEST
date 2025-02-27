a, b, c = map(int, input().split())

# Please write your code here.
day = 11 
hour = 11
mint = 11

cur_state =  11*24*60+11*60+11 
goal_state = a*24*60+b*60+c 
ans = goal_state-cur_state if goal_state-cur_state >=0 else -1
print(ans)
