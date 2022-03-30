def transpose(l):
    j=[]
    for i in range (0,len(l[0])):
        for g in range(0,len(l)):
            j[i][g]=l[g][i]
    print(j)    
l=[[1,3,5],[4,6,8]]
transpose(l)
