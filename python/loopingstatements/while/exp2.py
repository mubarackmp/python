# Q1

# l=[]
# n=3
# i=0
# z=0
# while z<n:
#     m=str(input("enter string""\n"))
#     l.append(m)
#     z=z+1
# while i<len(l):
#     print(l[i],len(l[i]))
#     i=i+1

# Q2

# a=str(input("enter a string""\n"))
# b={}
# i=0
# while i<len(a):
#     if a[i] in b:
#         b[a[i]]+=1
#     else:
#         b[a[i]]=1
#     i+=1
# print(b)

# Q3

# l1=[]
# l2=[]
# l3=[]
# n=4
# i=0
# z=0
# y=0
# while z<n:
#     m=str(input("enter first list of num"))
#     l1.append(m)
#     z=z+1
# while y<n:
#     s=str(input("enter second list of  num"))
#     l2.append(s)
#     y=y+1
# while i<len(l1):
#     if l1[i] in l2:
#         l3.append(l1[i])
#     i=i+1
# print(l1)
# print(l2)
# print(l3)


# Q4

# a=str(input("enter a string""\n"))
# b=""
# i=len(a)-1
# while i>=0:
#     b=b+a[i]
#     i=i-1
# print(b)


# Q5

# a=int(input("enter the limit"))
# l=[]
# i=1
# sum=0
# while i<=a:
#     m=int(input("enter the list of numbers"))
#     l.append(m)
#     sum=sum+m
#     i=i+1
# print(l)
# print(sum)

# Q6

# l1=[]
# l=0
# n=4
# i=0
# z=0
# while z<n:
#     m=int(input("enter first list of num"))
#     l1.append(m)
#     z=z+1
# while i<len(l1):
#     if l1[i]>l1[i-1]:
#         l=l1[i]
#     i=i+1
# print(l1)
# print(l)


# Q7

# a=str(input("enter a string""\n"))
# b=1
# i=0
# while i<len(a):
#     if a[i].isalpha():
#         pass
#     else:
#         b=b+1
#     i=i+1
# print(b)



# Q8

# l=[]
# l2=[]
# n=5
# i=0
# z=0
# while z<n:
#     m=str(input("enter string""\n"))
#     l.append(m)
#     z=z+1
# while i<len(l):
#     if len(l[i])>=5:
#         l2.append(l[i])
#     i=i+1
# print(l2)



# Q9

# a=int(input("enter the limit"))
# l=[]
# l2=[]
# i=1
# while i<=a:
#     m=int(input("enter the list of numbers"))
#     l.append(m)
#     if m%2==0:
#         l2.append(m)
#     i=i+1
# print(l)
# print(l2)


# Q10

# l=[]
# l2=[]
# n=3
# i=0
# z=0
# while z<n:
#     m=str(input("enter string""\n"))
#     l.append(m)
#     l2.append(m[0].upper()+m[1:])
#     z=z+1
# print(l)
# print(l2)
