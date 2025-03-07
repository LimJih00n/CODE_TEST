'''
예산이 b만큼 있음
Pi씩 원함
하나는 반값으로 할인 가능
what? 선물 가능한 최대 명수
how: 가장 간단: 1~i까지 모두 쓰면서 자기 예산보다 작을 수 있는지 확인 정렬후에 예산안에서 빼면서 확인하기
'''
N,B = map(int,input().split())
P = [int(input()) for i in range(N)]
ans = 0
for i in range(N):
    P_cur,B_cur = P[:],B 
    P_cur[i] //= 2
    P_cur.sort()
    count = 0 
    for p in P_cur:
        if B_cur - p >0:
            B_cur -= p 
            count +=1
        else:
            break
    ans = max(ans,count)
print(ans)
