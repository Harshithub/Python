def insertionsort(l):
    for i in range(len(l)):
        while i>0 and l[i]<l[i-1]:
            (l[i],l[i-1])=(l[i-1],l[i])
            i=i-1
    print(l)
l=[]    
print("enter size of list")
n=int(input())
for i in range(0,n):
    x=int(input("enter value "))
    l.append(x)
insertionsort(l)
          
