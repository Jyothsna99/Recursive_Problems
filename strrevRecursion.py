#Iterative Approach to reverse a given String
def itrev(s):
    r=""
    for i in s:
        r=i+r
    return r

'''def rerev(n,l):
    s=""
    if l==0:
        return n[l]
    else:
        s=s+n[l]+rerev(n,l-1)
    return s'''
#Recursive Approach to reverse a given String
def rerev(s): 
    if len(s) == 0: 
        return s 
    else: 
        return rerev(s[1:]) + s[0] 


if __name__=='__main__':
    import timeit
    n=input()#input a String
    start=timeit.default_timer()
    print(rerev(n))
    end=timeit.default_timer()
    print("Time taken in seconds is:",end-start)