def recount(l,n):
    '''Number of elements in a list using Recursion'''
    if len(l)==0:
        return 0
    else:
        if l[-1]==n:
            return 1+recount(l[:-1],n)
        else:
            return recount(l[:-1],n)
if __name__=='__main__':
    n=int(input())
    l=eval(input())
    print(recount(l,n))