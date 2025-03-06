n = int(input())
arr = input()

# Please write your code here.
'''
what? COW 의 경우의 수 구학. COW가 이어져야함.
how: 가능한 모든 조합 만들고 COW인지 확인하기.
조합 만들기 -> 반복문 or dfs
'''
def gen_p(elements,r):
    re = []
    visits = [0] * len(elements)
    def dfs(path):
        if len(path) == r:
            re.append(path[:])
            return
        for i in range(len(elements)):
            if not visits[i]:
                visits[i] = 1
                path.append(elements[i])
                dfs(path)
                path.pop()
                visits[i] = 0
    dfs([])
    return re
elements = [i for i in range(n)]
ans = 0
cases = gen_p(elements,3)
for c in cases:
    if (arr[c[0]]+arr[c[1]]+arr[c[2]]) == "COW":
        ans +=1
print(ans)



