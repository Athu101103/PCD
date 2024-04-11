// to associate postfix notation of the given arithmetic expression with every node
// in the parse tree.

from collections import *

class Node:
  def __init__(self, value=None, left=None, right=None, next=None, postfix=None):
    self.value=value
    self.left=left
    self.right=right
    self.next=next
    self.postfix=postfix


class Stack:
  def __init__(self):
    self.top=None

  def push(self,new_node):
    if(not self.top): #stack is empty
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
    print(p.value,end="\t")
    print(p.postfix)
    self.inorder(p.right)


precedence={'*':2,"/":2,"+":1,"-":1}

expr="((a+b)*(a-b))"

print("Input expression:", expr)
print("\n")

stack=[]
postfix=[]

#infix to postfix

for i in range(len(expr)):

  if(expr[i]=='('):
    stack.append(expr[i])

  if(expr[i].isalpha()):
    postfix.append(expr[i])

  elif(expr[i] in list(precedence.keys()) and stack[-1]=='('):
    stack.append(expr[i])

  elif (expr[i] in list(precedence.keys()) and stack[-1] in list(precedence.keys())):
    if(precedence[expr[i]] > precedence[stack[-1]]):
      stack.append(expr[i])

    else:
      while (len(stack) and stack[-1]!='(' and stack[-1]!=')' and precedence[stack[-1]]>= precedence[expr[i]] ):
        postfix+=(stack.pop())

      stack.append(expr[i])

  elif(expr[i]==')'):
    if(len(stack)!=0):
      while(True):
        elt=stack.pop()
        if(elt=='('):
          break
        postfix+=elt

print("Postfix expression:", postfix)


#postfix to syntax tree

operators=list(precedence.keys())
tree_stack=Stack()

syntax_tree=Tree()

for c in postfix:

  if(c in operators):
    op2=tree_stack.pop()
    op1=tree_stack.pop()

    op_node=Node()
    op_node.value=c
    op_node.postfix=op1.postfix+op2.postfix+c
    op_node.left=op1
    op_node.right=op2
    tree_stack.push(op_node)

  if (c.isalpha()):
    new_node=Node()
    new_node.value=c
    new_node.postfix=c
    tree_stack.push(new_node)

root=tree_stack.pop()
print("\nINORDER TRAVERSAL")
syntax_tree.inorder(root)

