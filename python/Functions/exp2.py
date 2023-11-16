def capitailed():
    l2=[]
    i=0
    m=str(input("enter string""\n"))
    n=m.split()
    while i<len(n):
        b=n[i]
        l2.append(b[0].upper()+b[1:])
        i+=1
    st=" ".join(l2)
    print(st)

def spclrmvd():
    a=str(input("enter a string""\n"))
    b=""
    i=0
    while i<len(a):
        if a[i].isalpha():
            b=b+a[i]
        i=i+1
    print(b)

def square():
    l=[]
    l2=[]
    n=4
    for i in range(n):
        a=int(input("enter the numbers""\n"))
        l.append(a)
        l2.append(a**2)
    print(l)
    print(l2)

def sumofsqr():
    a=int(input("enter the numbers""\n"))
    b=a%10
    c=a//10
    d=c%10
    e=c//10
    sum=(b**2)+(d**2)+(e**2)
    print(sum)

def commenelements():
        
    l1=[]
    l2=[]
    l3=[]
    n=4
    i=0
    z=0
    y=0
    while z<n:
        m=str(input("enter first list of num"))
        l1.append(m)
        z=z+1
    while y<n:
        s=str(input("enter second list of  num"))
        l2.append(s)
        y=y+1
    while i<len(l1):
        if l1[i] in l2:
            l3.append(l1[i])
        i=i+1
    print(l1)
    print(l2)
    print(l3)

# Q1
# capitailed()

# Q2
# spclrmvd()

# Q3
# square()

# Q4
# sumofsqr()

# Q5
# commenelements()