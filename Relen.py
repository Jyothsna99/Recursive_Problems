def relen(s):
    '''length of a string using Recursion'''
    if s=="":
        return 0
    else:
       return relen(s[1:])+1
if __name__=='__main__':
    l=[x for x in input().split()]
    print(relen(l))