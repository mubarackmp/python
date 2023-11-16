# function program

# function declaration  
def pattern1():  
    # function definition 
    k=1
    for i in range(6):
        for j in range(1,k+1):
            print("*",end=" ")
        k+=2
        print()

def pattern2():
    for i in range(10):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

# function call 

# pattern1()
# pattern2()
