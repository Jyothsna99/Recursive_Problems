def odd(n):
    '''sum of odd numbers upto n'''
    if n==1:
        return 1
    elif n%2==1:
        return n+odd(n-2)
    else:
        return odd(n-1)
    
        