#recusive function to find factorial of a number
def refib(n):
    if n==0 or n==1:
        return n
    else:
        return refib(n-1)+refib(n-2)
#recusive function to find factorial of a number
def itfib(n):
    a=0;b=1
    c=a+b
    f=3
    while(f<=n):
        a=b
        b=c
        c=a+b
        f+=1
    return c
    
if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    print(refib(n))
    print(itfib(n))
    end=timeit.default_timer()
    print("Time taken in seconds is:",end-start)
        