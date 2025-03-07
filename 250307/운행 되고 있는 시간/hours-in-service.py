# Please write your code here.
'''
문제를 더 자세하게 읽기
A<= x < B
what? 한명을 제외하였을때 시간합이 최대가 되게 하는 것.
t1, t2가 이어짐을 확인
=> t1[1]>=t2[0]
tuple정렬 Please write your code here.
아 근데 한명이라도 일하고

how?
tuple정렬하기
한명을 제외하였을때 
그냥 1000 1로 채워두고 연속되는 1의 개수 구하기.
하나씩 지워보며 반복.
'''
N = int(input())
work_time_list = [tuple(map(int,input().split())) for i in range(N)]

work_time_list=sorted(work_time_list,key=lambda x : x[0])

def check_time(arr):
    re = 0 
    count = 0
    for i in range(1,1001):
        if arr[i] >= 1:
            count +=1
    return count
'''
1~2 / 2~3 / 3~4 / 4~5 
 1    1      1     0
'''
ans = 0
for i in range(N):
    arr = work_time_list[:]
    del arr[i]
    check_arr = [0]*1001
    
    
    for s,e in arr:
        for j in range(s,e):
            check_arr[j] += 1
    #print(check_arr)
    ans=max(ans,check_time(check_arr))

print(ans)

