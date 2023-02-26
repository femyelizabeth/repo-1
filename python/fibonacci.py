#nth term of fibonacci series
#nth term of fibonacci series with dynamic pgmg(given the values for strting nd ending

#nth term
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter the limit:"))
print(fibo(n-1))

#dynamic pgmg
dp=[0]*100
dp[0]=0
dp[1]=1
dp[2]=1

def fibo(num):

    if num<=0:
        return dp[0]
    if num==1:
        return dp[1]
    if dp[num]!=0:
        return dp[num]
    dp[num]=fibo(num-1)+fibo(num-2)
    return dp[num]

num=int(input("Enter the limit:"))
print(fibo(num-1))
