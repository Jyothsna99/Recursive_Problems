#recusive function to find factorial of a number
def refact(n):
    if n==1:
        return 1
    else:
        x=n*refact(n-1)
    return x

  #Iterative function to find factorial of a number  
def itfact(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f


if __name__=='__main__':
    import timeit
    n=int(input())
    start=timeit.default_timer()
    refact(n)
    itfact(n)
    end=timeit.default_timer()
    print("Time taken in seconds is:",end-start)