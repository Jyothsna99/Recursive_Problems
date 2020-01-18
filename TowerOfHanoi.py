def toh(n,frm,to,aux):
    if n==1:
        print("move %d disk from %s to %s using %s as helper tower"%(n,frm,to,aux))
    else:
        toh(n-1,frm,aux,to)
        print("move %d disk from %s to %s using %s as helper tower"%(n,frm,to,aux))
        toh(n-1,aux,to,frm)
        
    