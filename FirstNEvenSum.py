def even(n):
    '''sum of first n even numbers'''
    if n==0:
        return 0
    else:
        return (n*2)+even(n-1)
    
if __name__=='__main__':
    n=int(input())
    print(even(n))
    
        