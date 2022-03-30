def repeated(l):
  new=[]
  for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] not in new and l[i]==l[j]:
            flag=1
    if flag=0:    
  return(new)
