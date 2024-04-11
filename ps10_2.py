//program to associate three address code of arithmetic expression (integer data types
//and mixed data types) with each node in the parse tree.

#Intermediate code generation

precedence={'+':1,'-':1, '*':2, "/":2}
operators=list(precedence.keys())

class Node:
  def __init__(self,value=None,left=None,right=None,codeid=None, code_label=None, code=None, mode=None,next=None):
    self.value=value
    self.left=left
    self.right=right
    self.codeid=codeid
    self.code_label=code_label
    self.code=code
    self.mode=mode
    self.next=next

class Stack:
  def __init__(self):
    self.top=None

  def push(self,new_node):
    if(not self.top):
      self.top=new_node

    else:
      new_node.next=self.top
      self.top=new_node

  def pop(self):
    if(not self.top):
      print("Stack is empty!")

    else:
      popped=self.top
      self.top=self.top.next
      return popped

class Tree:
  def inorder(self,p):
    if(not p):
      return

    self.inorder(p.left)
    if(p.value in operators):
      print(p.value, end="\t")
      print(p.code)
    else:
      print(p.value)

    self.inorder(p.right)


  def postorder(self,p):
    if(not p):
      return

    self.postorder(p.left)
    self.postorder(p.right)
    if(p.value in operators):
      print(p.value, end="\t")
      print(p.code)
      print("mode:",p.mode)
      print("\n")
    else:
      print(p.value)
      print("mode:",p.mode)
      print("\n")

input="( 1 / ( 2.5 + ( 3 * 9.0 ) ) )"
expr=input.split()
print(expr)


#infix to postfix
stack=[]
postfix=[]

for i in range(len(expr)):
  if(expr[i]=='('):
    stack.append('(')

  elif(expr[i] not in operators and expr[i]!=')'):
    postfix.append(expr[i])

  elif(expr[i] in operators and stack[-1]=='('):
    stack.append(expr[i])

  elif(expr[i] in operators and stack[-1] in operators):
    if(precedence[expr[i]] > precedence[stack[-1]]):
      stack.append(expr[i])

    else:
      while(len(stack) and stack[-1]!='(' and stack[-1]!=')' and precedence[expr[i]]<=precedence[stack[-1]]):
        postfix+=(stack.pop())

      stack.append(expr[i])

  elif(expr[i]==')'):
    if(len(stack)!=0):
      while(True):
        elt=stack.pop()

        if(elt=='('):
          break
        postfix+=(elt)


print(postfix)

#tree construction

tree_stack=Stack()
syntax_tree=Tree()


code_id=-1

for c in postfix:
  if(c in operators):
    new_node=Node()
    new_node.value=c
    op2=tree_stack.pop()
    op1=tree_stack.pop()
    new_node.codeid=code_id+1
    new_node.code_label="T"+str(new_node.codeid)
    new_node.code=new_node.code_label+" = " + op1.code_label + " " +  c + " " + op2.code_label

    if(op1.mode=="real" or op2.mode=="real"):
      new_node.mode="real"

    elif(op1.mode=="int" and op2.mode=="int"):
      new_node.mode="int"


    new_node.left=op1
    new_node.right=op2
    tree_stack.push(new_node)
    code_id=code_id+1

  else:
    new_node=Node()
    new_node.value=c
    if('.' in c):
      new_node.mode="real"
    else:
      new_node.mode="int"
    new_node.codeid=-1
    new_node.code_label=c
    new_node.code=""
    tree_stack.push(new_node)

root=tree_stack.pop()

print("\n\n\n")


print("POSTORDER TRAVERSAL OF THE SYNTAX TREE \n")
syntax_tree.postorder(root)
