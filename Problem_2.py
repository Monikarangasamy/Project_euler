#Problem number 2
#Even Fibonacci Numbers

def Fibonacci():
    a=1
    b=2
    ans=0
    while(a<=4*10**6):
        if a%2==0:
            ans+=a
        c=a+b
        a=b
        b=c
        
    return ans
print(Fibonacci())

