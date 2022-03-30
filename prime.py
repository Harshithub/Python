def prime(n):
    j=0
    if n==1:j=1
    if n==2:
        j=0
    if n>2:
        for i in range(2,n):
            if n%i==0:
                j=1;    
    if j==1:print("Not Prime")
    else:print("Prime")
            
prime(1)     
