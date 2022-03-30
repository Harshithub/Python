def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j<m+n:
        if i==m:
            c.append(b[j])
            j=j+1
        elif j==n:
            c.append(a[i])
            i=i=i+1
        elif a[i]>=b[j]:
            c.append(b[j])
            j=j+1
        elif a[i]<b[j]:
            c.append(a[i])
            i=i+1
    return(c)

            
