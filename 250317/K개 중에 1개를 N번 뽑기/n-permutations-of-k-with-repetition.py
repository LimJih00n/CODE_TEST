'''
1이상 K이하의 숫자를 하나 고르는 행위를 N 번 반복하여
나올 수 있는 모든 서로 다른 순서쌍을 고르는 프로그램
=> 중복순열
'''

def gen_p(elements,r):
    re = []
    
    def dfs(path):
    
        if len(path) == r:
            re.append(path[:])
            return

        for i in range(len(elements)):
            
                
            path.append(elements[i])
            dfs(path)
            path.pop()
    dfs([])
    return re 

K,N = map(int,input().split())
arr = [i+1 for i in range(K)]

ans = gen_p(arr,N)


for ele in ans:
    print(*ele)