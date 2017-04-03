link of question-https://www.hackerrank.com/challenges/ncr-table
def ncr(n):
    
    result=1
    for i in range(n//2):
        print(result%10**9,end=" ") 
        result=(result*(n-i))//(i+1)
    print(result%10**9,end=" ")        
    if(n%2==1 and n>1):
        print(result%10**9,end=" ")
    for j in range(n//2-1,0,-1):
        
        result=(result*(j+1))//(n-j)
        print(result%10**9,end=" ")
    print(1)
n=int(input("enter"))
ncr(n)
