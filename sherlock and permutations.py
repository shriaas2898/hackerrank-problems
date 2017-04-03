import math
T=int(input())
for i in range(T):
    n,m=list(map(int,input().split()))
    m-=1
    print(int(math.factorial(n+m)//(math.factorial(m)*math.factorial(n)))%int(10**9+7))
