# Q1

# for i in range(1,10):
#     k=65
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print() 



# Q2


# k=65
# for i in range(1,6):  
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print() 



# Q3

# k=65
# for i in range(1,6):  
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k+=1
#     print() 



# Q4

# for i in range(64,70):
#     for j in range(i+1,64,-1):
#         print(chr(j),end=" ") 
#     print()


# Q5

# n=6
# for i in range(6):
#     for k in range(0,n):
#         print(end="  ")
        
#     n-=1
#     print("*",end=" ")
#     for j in range(1,i+1):
#         print(chr(65),end=" ")
#         print("*",end=" ")
        
#     print()
 

# Q6

# n=6
# for i in range(6):
#     for k in range(0,n):
#         print(end="  ")   
#     n-=1
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for m in range(i-1,0,-1):
#         print(m,end=" ")
#     print() 


# Q7

# for i in range(0,9):
#     if i==0 :
#         print("*",end=" ")
#     if i==1:
#         print(1,end=" ")
#     if i>1 and i%2==0:
#         for j in range(0,i):
#             print("*",end=" ")
#     if i>2 and i%2==1:
#         for k in range(1,i):
#             print(k,end=" ")
#     print()
        


# Q8


# b=4
# a=(b*2)+1
# for i in range(a):
#     for k in range(0,1):
#         print("*",end=" ") 
#     if i<b:
#         for j in range(1,i+1):
#             print(j,end=" ")
#         for m in range(i-1,0,-1):
#             print(m,end=" ")
#     if i>=b:
        
#         for n in range(1,b):
#             print(n,end=" ")
#         for o in range(b,0,-1):
#             print(o,end=" ")
#         b=b-1
#     if i>0 and i<a-1:
#         for l in range(0,1):
#             print("*",end=" ")
#     print()
#     print() 





# Q9


# for i in range(8):
#     if i%2==0:
#         for l in range(i-1,0,-1):
#             print("*",end=" ")
#         print()
#         for j in range(i-1,0,-1):
#             print(j,end=" ")
#     if i%2==1:
#         for m in range(1,i):
#             print("*",end=" ")
#         print()
#         for k in range(1,i):
#             print(k,end=" ")
#     print()
