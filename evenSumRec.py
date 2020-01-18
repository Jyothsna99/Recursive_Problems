def even(n):
    '''sum of even numbers upto n'''
    if n==2:
        return 2
    elif n%2==0:
        return n+even(n-2)
    else:
        return even(n-1)
    
if __name__=='__main__':
    n=int(input())
    print(even(n))
    
        