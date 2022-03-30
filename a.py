
def primeproduct(m):
  flag=flag2=1
  
  if m>1 :
    for i in range(2,m-1,1):
      if m%i==0:
        for j in range(2,i-1):
          if i%j==0:
              flag=0
        if flag==1:
          c=int(m/i)
          for j in range(2,c-1,1):
            if c%j==0:
                flag2=0
      i=m-1        
    if flag==1 and flag2==1:
      print('True')
    else :
      print('False')
  else:
    print('False')

primeproduct(6)

