def selection(l):
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if l[i]>l[j]:
                (l[i],l[j])=(l[j],l[i])
    print(l)
n= int(input("enter size of list"))
l=[]
for i in range(0,n):
    x=int(input())
    l.append(x)
selection(l)
