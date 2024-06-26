from prettytable import PrettyTable

exp = input("Enter arithmetic expression with appropriate brackets: ")
print("\nARITHMETIC EXPRESSION: ", exp)

operators=['*','+','-','/']
asg = exp[0]
stack = []


#print("ASG: ", asg)
#print("EXP: ", exp)

int_code = {}
count = 0

for i in range(len(exp)):
    if exp[i] == ')':
        s = ''
        while stack[-1] != '(':
            s = stack.pop()+s
        stack.pop()  # Remove the '('

        count += 1
        temp_var = 'T' + str(count)
        int_code[temp_var] = s
        stack.append(temp_var)
    else:
        stack.append(exp[i])

int_code[asg]='T'+str(count)

print("\n\nFinal Three Address Code:\n")
for key, value in int_code.items():
    print(key, '=', value)

op=[]
arg1=[]
arg2=[]
res=[]
print("\n\nQUADRAPLES\n")
for k,v in int_code.items():

  if v[0]=='-':
    op.append(v[0])
    arg1.append(v[1:])
    arg2.append('-')
    res.append(k)
  else:
    flag=0
    for i in operators:
      if i in v:
        flag=1
        ind=v.index(i)
        op.append(v[ind])
        arg1.append(v[0:ind])
        arg2.append(v[ind+1:])
        res.append(k)
        break
    if flag==0:
      op.append('=')
      arg1.append(v)
      arg2.append('-')
      res.append(k)

table=PrettyTable(['OPERATOR','ARG1','ARG2','RESULT'])

for i in range(len(op)):
  table.add_row([''.join(op[i]),''.join(arg1[i]),''.join(arg2[i]),''.join(res[i])])

print(table)

#A=((A+(B*C))-D)
#A=((-B)+(C*D))



# Three address code - TRIPLES

from prettytable import PrettyTable

exp = input("Enter arithmetic expression with appropriate brackets: ")
print("\nARITHMETIC EXPRESSION: ", exp)

operators=['*','+','-','/']
asg = exp[0]
stack = []

#print("ASG: ", asg)
#print("EXP: ", exp)

int_code = {}
count = 0

for i in range(len(exp)):
    if exp[i] == ')':
        s = ''
        while stack[-1] != '(':
            s = stack.pop()+s
        stack.pop()  # To Remove '('

        count += 1
        temp_var ='('+ str(count)+')'
        int_code[temp_var] = s
        stack.append(temp_var)
    else:
        stack.append(exp[i])

int_code[asg]='('+ str(count)+')'

print("\n\nFinal Three Address Code:\n")
for key, value in int_code.items():
    print(key, '=', value)

op=[]
arg1=[]
arg2=[]

print("\nTRIPLES\n")
for k,v in int_code.items():

  if v[0]=='-':
    op.append(v[0])
    arg1.append(v[1:])
    arg2.append('-')
  else:
    flag=0
    for i in operators:
      if i in v:
        flag=1
        ind=v.index(i)
        op.append(v[ind])
        arg1.append(v[0:ind])
        arg2.append(v[ind+1:])
        break
    if flag==0:
      op.append('=')
      arg1.append(k)
      arg2.append(v)

table=PrettyTable(['OPERATOR','ARG1','ARG2'])

for i in range(len(op)):
  table.add_row([''.join(op[i]),''.join(arg1[i]),''.join(arg2[i])])

print(table)


#A=((A+(B*C))-D)
#A=((-B)+(C*D))