'''
x<=n<=y
what?다른 모든 자리는 같고 한자리만 다른 수 의 개수 찾기
how?
list 만들기 2d
0: 등장
1: 횟수
sum[0] = > 2
in [1] 횟수: 1이 무조건 있어야한다. 
'''

X,Y = map(int,input().split())
check_arr = [[0]*10 for i in range(2)]

def check_con(arr):
    if sum(arr[0]) == 2 and 1 in arr[1]:
        return True
    return False
ans = 0
for num in range(X,Y+1):
    arr = [[0]*10 for i in range(2)]
    for n in str(num):
        arr[0][int(n)] = 1
        arr[1][int(n)] +=1
    
    if check_con(arr):
        ans +=1
print(ans)
        
