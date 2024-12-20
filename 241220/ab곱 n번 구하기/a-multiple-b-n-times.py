n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    m_ = 1
    for i in range(a,b+1):
        m_*=i
    print(m_)