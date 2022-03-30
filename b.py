
def delchar(str1,s):
    b=""
    a=len(str1)
    for i in range(0,a,1):
      if str1[i]!=s:
          b=b+str1[i]
    print (b)     
    
    
delchar("banana","an")
