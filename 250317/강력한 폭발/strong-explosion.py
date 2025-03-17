'''
what? 1이 놓인 위치에서 특정위치에 색을 칠했을때
가장 많이 칠할 수 있는 거 구하기

how?
1. 폭탄 터짐 표시할 배열 만들기
2. 그 경우를 모두 구하기 즉 1의 개수에서 폭탄이 특정일때의 변수를 모두 구해야함
=> 중복 순열
case1
case2
case3 

그리고 색깔 너비 구하기.
색칠할때 범위 주위!

'''
import copy

boom_dic={
    "c1":[(-2,0),(-1,0),(1,0),(2,0)],
    "c2":[(1,0),(-1,0),(0,-1),(0,1)],
    "c3":[(1,1),(-1,-1),(1,-1),(-1,1)]
}
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
boam_pos = [(i,j) for i in range(N) for j in range(N) if arr[i][j] == 1]
boam_conut = len(boam_pos)

def gen_h(ele,r):
    re =[]
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

# 1번 2번 n번 폭탄의 상태라 가정함. 

cases = gen_h(["c1","c2","c3"],boam_conut)
ans = 0
for case_ in cases:
    after_boam = copy.deepcopy(arr)
    for i in range(len(boam_pos)):
        cur_pos = boam_pos[i]
        for po in boom_dic[case_[i]]:
            if cur_pos[0] + po[0] >=N or cur_pos[1] + po[1] >=N or cur_pos[1] + po[1] <0 or cur_pos[0] + po[0] <0:
                continue
            nr = cur_pos[0]+po[0]
            nc = cur_pos[1]+po[1]
            if (nr,nc) not in boam_pos:
                after_boam[nr][nc] = 2
    
    
    ans = max(ans,sum([1 for r in range(N) for c in range(N) if after_boam[r][c]==2])+len(boam_pos))
print(ans)
