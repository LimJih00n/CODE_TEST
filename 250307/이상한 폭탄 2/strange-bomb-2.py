

# Please write your code here.
'''
what? 같은 번호가 부여된 폭탄끼리 거리가 K안에 있으면 폭파된다.
거리가 K안에 있는 같은 번호의 폭탄은 모두 터지는데 그 번호가 가장 큰 거 구하기
폭발할 폭탄 중에 가장 큰 번호를 출력하는 프로그램 만들기 

how? 
1. 폭탄 순회, 
2. 거리 +- k 순회, 
3. 자기랑 같은 번호 있으면 터지기 번호 max 경신

'''
N,k = map(int,input().split())
boams = [int(input()) for i in range(N)]
ans = -1
for i in range(N):
    s = i-k if i-k < 0 else 0
    e = i+k if i+k < N else N
    boam_num = boams[i]
    for j in range(s,e):
        if i==j:
            continue
        if boams[j]==boams[i]:
            ans = max(ans,boam_num)
print(ans)
