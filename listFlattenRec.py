def flatten(l):
    '''input=[[[2,3,3]][3,4][5]]
    output=[2,3,3,3,4,5]'''
    nl=[]
    for x in l:
        if type(x)!=list:
            nl.append(x)
        else:
            nl.extend(flatten(x))
    return nl
if __name__=='__main__':
    l=input()
    print(flatten(l))