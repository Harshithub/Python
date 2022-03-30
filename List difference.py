def listdifference(a,b):
    (c,i,j)=([],0,0)
    (m,n)=(len(a),len(b))
    while i+j<m+n:
       if i==m:
            j=j+1
       elif j==n:
            c.append(a[i])
            i=i+1
       elif a[i]!=b[j]:
            if a[i]<b[j]:
                c.append(a[i])
                i=i+1
            elif a[i]>b[j]:
                j=j+1
       elif a[i]==b[j]:
            j=j+1
            i=i+1
    return(c)

