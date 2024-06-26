# -*- coding: utf-8 -*-
"""ws_8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/134p9yxecGbZwOoYgmjahaO4gL4l4yyEj

---

> **1. Write a program to remove left recursion (Both immediate and indirect) from the given grammar.**





---
"""

def remove_left_recursion(grammar):
    non_terminals = list(grammar.keys())
    new_grammar = {}

    for A in non_terminals:
        new_grammar[A] = []
        alpha = []
        beta = []

        for production in grammar[A]:
            if production[0] == A:
                alpha.append(production[1:])
            else:
                beta.append(production)

        if len(alpha) > 0:
            new_non_terminal = A + "'"
            new_grammar[new_non_terminal] = [a + new_non_terminal for a in alpha] + ['e']
            new_grammar[A] = [b + new_non_terminal for b in beta]
        else:
            new_grammar[A] = grammar[A]

    return new_grammar


def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(non_terminal + " -> " + " | ".join(productions))


# Example grammar
grammar = {
    "S": ["S+T", "T"],
    "T": ["T*F", "F"],
    "F": ["a"]
}

print("Original Grammar:")
print_grammar(grammar)

new_grammar = remove_left_recursion(grammar)

print("\nGrammar after removing left recursion:")
print_grammar(new_grammar)

"""
---

> **2. Write a program to apply left factoring on the grammar.**





---

"""

from itertools import takewhile
def groupby(ls):
    d = {}
    ls = [ y[0] for y in rules ]
    initial = list(set(ls))
    for y in initial:
        for i in rules:
            if i.startswith(y):
                if y not in d:
                    d[y] = []
                d[y].append(i)
    return d

def prefix(x):
    return len(set(x)) == 1


starting=""
rules=[]
common=[]
alphabetset=["A'","B'","C'","D'","E'","F'","G'","H'","I'","J'","K'","L'","M'","N'","O'","P'","Q'","R'","S'","T'","U'","V'","W'","X'","Y'","Z'"]


s= "S->iEtS|iEtSeS|a"
print()
print("Grammar before left factoring : ")
s1= "S->iEtS | iEtSeS | a"
print(s1)
print()
print("Grammar after left factoring : ")
while(True):
    rules=[]
    common=[]
    split=s.split("->")
    starting=split[0]
    for i in split[1].split("|"):
        rules.append(i)

    for k, l in groupby(rules).items():
        r = [l[0] for l in takewhile(prefix, zip(*l))]
        common.append(''.join(r))
    for i in common:
        newalphabet=alphabetset.pop()
        print(starting+" -> "+i+newalphabet)
        index=[]
        for k in rules:
            if(k.startswith(i)):
                index.append(k)
        print(newalphabet+" -> ",end="")
        for j in index[:-1]:
            stringtoprint=j.replace(i,"", 1)+"| "
            if stringtoprint=="| ":
                print("\u03B5","| ",end="")
            else:
                print(j.replace(i,"", 1)+"| ",end="")
        stringtoprint=index[-1].replace(i,"", 1)+"| "
        if stringtoprint=="| ":
            print("\u03B5","",end="")
        else:
            print(index[-1].replace(i,"", 1)+" ",end="")
        print("")
    break

"""
---

> **3. Write a program to find first and follow for the non-terminals in the given grammar.**





---

"""

print("Recursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'/e\nT->FT'\nT'->*FT'/e\nF->(E)/i\n")
print("Enter the string want to be checked\n")
global s
s=list(input())
global i
i=0
def match(a):
    global s
    global i
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True
    else:
        return False
def F():
    if(match("(")):
        if(E()):
            if(match(")")):
                return True
            else:
                return False
        else:
            return False
    elif(match("i")):
        print('i')
        return True
    else:
        return False
def Tx():
    if(match("*")):
        print('*')
        if(F()):
            if(Tx()):
                return True
            else:
                return False
        else:
            return False
    else:
        return True
def T():
    if(F()):
        if(Tx()):
            return True
        else:
            return False
    else:
        return False
def Ex():
    if(match("+")):
        print('+')
        if(T()):
            if(Ex()):
                return True
            else:
                return False
        else:
            return False
    else:
        return True
def E():
    if(T()):
        if(Ex()):
            return True
        else:
            return False
    else:
        return False
if(E()):

    if(i==len(s)):
        print("String is accepted")
    else:
         print("String is not accepted")

else:
    print("string is not accepted")

"""
---

> **4. Write a program to implement predictive parsing technique.**





---

"""

#Some helper functions
def print_iter(Matched,Stack,Input,Action,verbose=True):
    if verbose==True:
        print(".".join(Matched).ljust(30)," | ",".".join(Stack).ljust(25)," | ",".".join(Input).ljust(30)," | ",Action)
#The predictive parsing algorithm
def predictive_parsing(sentence,parsingtable,terminals,start_state="S",verbose=True):      #Set verbose to false to not see the stages of the algorithm
    status = None
    match = []
    stack = [start_state,"$"]
    Inp = sentence.split(".")
    if verbose==True:
        print_iter(["Matched"],["Stack"],["Input"],"Action")
    print_iter(match,stack,Inp,"Initial",verbose)
    action=[]
    while(len(sentence)>0 and status!=False):
        top_of_input = Inp[0]
        pos = top_of_input
        if stack[0] =="$" and pos == "$" :
            print_iter(match,stack,Inp,"Accepted",verbose)
            return "Accepted"
        if stack[0] == pos:
            print_iter(match,stack,Inp,"Pop",verbose)
            match.append(stack[0])
            del(stack[0])
            del(Inp[0])
            continue
        if stack[0]=="epsilon":
            print_iter(match,stack,Inp,"Poping Epsilon",verbose)
            del(stack[0])
            continue
        try:
            production=parsingtable[stack[0]][pos]
            print_iter(match,stack,Inp,stack[0]+" -> "+production,verbose)
        except:
            return "error for "+str(stack[0])+" on "+str(pos),"Not Accepted"

        new = production.split(".")
        stack=new+stack[1:]
    return "Not Accepted"

if __name__=="__main__":
    #Example for the working of the predictive parsing :-
    #input for the grammar : E->TE1;E1->+TE1|epsilon;T->FT1 ...
    parsingtable = {
    "E" : {"id" : "T.E1", "(" : "T.E1"},
    "E1" : {"+":"+.T.E1", ")":"epsilon", "$" : "epsilon"},
    "T" : {"id" : "F.T1", "(" : "F.T1" },
    "T1" : {"+" : "epsilon", "*" : "*.F.T1", ")" : "epsilon", "$" : "epsilon"},
    "F":{"id":"id","(":"(.E.)"}
    }
    terminals = ["id","(",")","+","*"]
    #Another Example done in class:-
    print(predictive_parsing(sentence="c.c.c.c.d.d.$",parsingtable={"S" : {"c":"C.C","d":"C.C"},"C":{"c":"c.C","d":"d"}},terminals=["c,d"],start_state="S"))