# Please write your code here.
'''
1-N 인접 
거리가 2이내에 있으면 열린다 => 1~N도 원형으로 연결됨 주의
두조합에 대해 자리가 거리가 2이하면 열림
9도 1에 가깝다를 어떻게알 수 있을까?
1 2 3 4 5 6 7 8 9 ... N-1 N 1 2 까지 가능. 

what? : 조합A와 조합 B가 주어졌을때 (3자리수임)
각 자리수의 차가 abs(2)이내인 조합의 수 구하기 A or B에 만족하면 된다.

how: 3자리수가 3자리수에 만족하는지 check condition 함수 만들기
 범위안에 있어야한다. + 1,2 N,N-1에 대해서는 따로 처리하기
 pre: n / a1,a2,a3 . 
 ex: n-2 <= a1 <= n+2.  if n 1,2,N,N-1일 경우 다르게
모든 경우에 대해 check condion 함수 진행 
'''
N = int(input())
a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())

def check_condition(n,a): #n 넣는 숫자, a 기준 숫자.

    if a == N:
        if n==N-1 or n== N-2 or n==N or n==1 or n==2:
            return True
    elif a==N-1:
        if n==N-2 or N-3==n or  n==N-1 or n==N or n==1:
            return True 
    elif a == 1:
        if n==N-1 or n== N or n==1 or n==2 or n==3:
            return True
    elif a==2:
        if  N==n or  n==1 or n==2 or n==3 or n==4:
            return True 
    else:
        if n-2 <= a <=n+2:
            return True
    return False
ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if (check_condition(i,a1) and check_condition(j,b1) and check_condition(k,c1)) or (check_condition(i,a2) and check_condition(j,b2) and check_condition(k,c2)):
                ans += 1
print(ans)