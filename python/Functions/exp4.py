
def noofwords():
    sen=str(input("enetr a sentence""\n"))
    n=sen.split()
    nofw=len(n)
    print(nofw)

def bigwordofsentence():
    sen=str(input("enetr a sentence""\n"))
    ns=sen.split()
    bigword=""
    size=0
    for i in range (len(ns)):
        word=ns[i]
        if len(word)>size:    
            bigword=word
            size=len(word)
    print(bigword,size,ns)

def capitalwords():
    sen=str(input("enetr a sentence""\n"))
    ns=sen.split()
    ls=[]
    for i in range (len(ns)):
        word=ns[i]
        wor=word[0].upper()+word[1:]
        if word==wor:
            ls.append(word)
    print(ls)

# Q1
# noofwords()

# Q2
# bigwordofsentence()

# Q3
# capitalwords()