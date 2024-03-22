
'''
5
E->E+T
E->T
T->T*F
T->F
F->a
+*a
a+a*a
'''

import numpy as np
def stringcheck():
    a=list(input("Enter the operator used in the given grammar "))
    a.append('$')
    print(a)
    l=list("abcdefghijklmnopqrstuvwxyz")
    o=list('(/*%+-)')
    p=list('(/*%+-)')
    n=np.empty([len(a)+1,len(a)+1],dtype=str,order="C")
    print(n)
    for j in range(1,len(a)+1):
        n[0][j]=a[j-1]
        n[j][0]=a[j-1]    
    for i in range(1,len(a)+1):
        l=1
        for j in range(1,len(a)+1):
            k=1
            n[i][j]=input(f"Enter the precedence of  {n[k][0]} and {n[0][l]}")
            k+=1
            l+=1
            
    print("The Operator Precedence Relational Table")
    print(n)
    i=list(input("Enter the string want to be checked "))
    i.append("$")
    s=[None]*len(i)
    q=0
    s.insert(q,"$")
    x=[row[0] for row in n]
    y=list(n[0])
    h=0
    while(s[0]!=s[1]):
        if((i[len(i)-2] in p)):
            break
        elif((s[q] in x)and(i[h]in y)):
            if(n[x.index(s[q])][y.index(i[h])]=="<"):
                q+=1
                s.insert(q,i[h])
                h+=1
            elif(n[x.index(s[q])][y.index(i[h])]==">"):
                s.pop(q)
                q-=1
            elif((n[x.index(s[q])][y.index(i[h])]=='')and ((s[q]=="$") and (i[h]=="$"))):
                s[1]=s[0]
        else:
            break
    if(s[0]!=s[1]):
        return False
    else:
        return True

def grammarcheck(i):
    print("Enter the",str(i+1)+"th production")
    b=list(input().split("->"))
    f=list("abcdefghijklmnopqrstuvwxyz")
    if(b[0]==" " or b[0]=="" or b[0] in f or len(b)==1):
        return False
    else:
        b.pop(0)
        b=list(b[0])
        s=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        o=list("(abcdefghijklmnopqrstuvwxyz^/*+-|),")
        sp=['!','@','#','$','?','~','`',',',';',':','"','=','_','&',"'",""," "]
        for i in range(0,len(b),2):
            if(b[i]==" "):
                g=False
            elif(b[i] in sp):
                g=False
                break
            elif(b[len(b)-1] in o and ((b[0]=="(" and b[len(b)-1]==")" )or (b.count("(")==b.count(")")))):
                g=True
            elif(b[i] in f):
                g=True
            elif(b[len(b)-1] in o):
                print("a")
                g=False
            elif((i==len(b)-1) and (b[i] in s)):
                g=True
            elif((i==len(b)-1) and (b[i] not in s) and (b[i] in o)and b[i-1] in o):
                g=True
            elif((b[i] in s) and(b[i+1]in o)):
                g=True
            elif((b[i] in s) and (b[i+1] in s)):
                g=False
                break
            else:
                g=False
                break
        if(g==True):
            return True
        else:
            return False
c=int(input("Enter the number of LHS variables "))
for i in range(c):
    if(grammarcheck(i)):
        t=True
    else:
        t=False
        break
if(t):
    print("Grammar is accepted")
    if(stringcheck()):
        print("String is accepted")
    else:
        print("String is not accepted")
        
else:
    print("Grammar is not accepted ")