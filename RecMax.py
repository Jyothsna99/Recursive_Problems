def maxl(l):
    '''maximum element in a list using recursion'''
    if len(l)==1:
        return l[0]
    else:
        return max(l[-1],maxl(l[:-1]))

if __name__=='__main__':
    l=[x for x in input().split()]
    print(maxl(l))