def factor(n,i=1):
    if i>n:return(1)
    else:
        if n%i==0:print(i)
        return factor(n,i+1)
    
factor(2000)

        
            
