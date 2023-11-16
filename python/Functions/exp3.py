def fibiniche():
    n=int(input("enter a positive intiger""\n"))
    fib=[0,1]
    a=0
    b=1
    for i in range(1,n):
        c=a+b
        fib.append(c)
        a=b
        b=c
    print(fib)

def sumof18pairs():
    l=[3,8,12,7,6,10,21,15]
    l2=[]
    i=0
    while i<len(l):
        b=l[i]
        a=18-b
        if a in l:
            l2.append((l[i],a))
        # print(l[i])
        # print(b)
        i+=1
    print(l2)

def pairofsamechrcts():
    l=["apple","banana","cherry","date","fgijk","kumnbvc"]
    l2=[]
    for i in range(len(l)):
        a=l[i]
        for j in range(len(l)):
            b=l[j]
            if a[i] in b[j]:
                l2.append((a,b))
    print(l2)

def proevensumodd():
    l=[2,3,4,5,6]
    l2=[]
    for i in range(len(l)):
        a=l[i]
        for j in range(len(l)):
            if (a*l[j])%2==0:
                if (a+l[j])%2==1:
                    l2.append((a,l[j]))
    print(l2)

# Q1
# fibiniche()

# Q2
# sumof18pairs()

# Q3
# pairofsamechrcts()

# Q4
# proevensumodd()