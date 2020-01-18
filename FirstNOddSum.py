def odd(n):
    '''sum of first n odd numbers'''
    if n==1:
        return 1
    else:
        return (n*2-1)+odd(n-1)
    
if __name__=='__main__':
    n=int(input())
    print(odd(n))
    
        