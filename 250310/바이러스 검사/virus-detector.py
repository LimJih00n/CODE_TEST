'''
팀장은 1명, 팀원은 여러명
가게당 팀장은 1명만 존재 무조건 필요 

how?
팀장 n명 필요. 따라서 팀장 만큼 인원 수 빼고
나머지는 주니어의 수로 채우면 된다.
'''
n = int(input())
arr = list(map(int,input().split()))
can_ = list(map(int,input().split()))
ans = n 
for i in range(n):
    arr[i] -= can_[0]
    if arr[i]<=0:
        continue
    ans += ( arr[i] // can_[1])
    if arr[i] % can_[1] !=0:
        ans+=1
print(ans)

