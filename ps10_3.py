from collections import defaultdict

binary_operator=["+","-","/","*","and","or",">","<","==","<=",">=","!="]
unary_operator=["not"]
precen={"or":1,"and":2,"==":3,"!=":3,">":4,"<":4,">=":4,"<=":4,"+":5,"-":5,"/":6,"*":6,"not":7}

class Node:
  def __init__(self,value=None,right=None,left=None,codeid=None,code=None,codelabel=None,next=None):
    self.value=value
    self.right=right
    self.left=left
    self.codeid=codeid
    self.code=code
    self.codelabel=codelabel
    self.next=next


class Stack:
  def __init__(self):
    self.top=None

  def push(self,node):
    if not self.top:
      self.top=node

    else:
      node.next=self.top
      self.top=node

  def pop(self):
    pop_node=self.top
    self.top=self.top.next
    return pop_node


class Syntax_tree:

  def inorder(self,root):
    if not root:
        return

    self.inorder(root.left)
    if root.value in binary_operator or root.value in unary_operator:
      print(root.value,end="\t")
      print(root.code,"\n")
      
    else:
      print(root.value,"\n")
    
    self.inorder(root.right)

  def postorder(self,root):
    if not root:
        return

    self.postorder(root.left)
    self.postorder(root.right)
    if root.value in binary_operator or root.value in unary_operator:
      print(root.value,end="\t")
      print(root.code,"\n")
      
    else:
      print(root.value,"\n")
    
    

def to_postfix(expression):
  stack=[]
  postfix=[]
  for i in expression:
    if i=="(":
      stack.append(i)
    elif i in binary_operator or i in unary_operator:
      while len(stack) and stack[-1] != "(" and stack[-1] != ")" and precen[stack[-1]]>=precen[i]:
        postfix.append(stack.pop())
      stack.append(i)
    elif i.isalpha():
      postfix.append(i)
    elif i==")":
      while len(stack):
        if stack[-1]=="(":
          stack.pop()
          break
        postfix.append(stack.pop())

  return postfix


def calculate_syntax(expression):
    syntax_tree=Syntax_tree()
    stack_list=Stack()

    id=-1
    for i in expression:
      if i in binary_operator:
        new_node=Node()

        op2=stack_list.pop()
        op1=stack_list.pop()

        new_node.value=i
        new_node.left=op1
        new_node.right=op2
        new_node.codeid=id+1
        new_node.codelabel="T"+str(new_node.codeid)
        new_node.code=new_node.codelabel+" = "+op1.codelabel+" "+i+" "+op2.codelabel

        stack_list.push(new_node)
        id+=1
      
      elif i in unary_operator:
        new_node=Node()

        op=stack_list.pop()

        new_node.value=i
        new_node.left=op
        new_node.codeid=id+1
        new_node.codelabel="T"+str(new_node.codeid)
        new_node.code=new_node.codelabel+" = "+i+" "+op.codelabel
        stack_list.push(new_node)
        id+=1

      else:
        new_node=Node()

        new_node.value=i
        new_node.codeid=-1
        new_node.codelabel=i
        new_node.code=""

        stack_list.push(new_node)
      
    root = stack_list.pop()
    print("postorder traversal")
    syntax_tree.postorder(root)

input_string="( x < y and y >= z or x == z and not w )"
input_list=input_string.split()
print("Given string")
print(input_string)
postfix=to_postfix(input_list)
print("Postfix")
print(postfix)
calculate_syntax(postfix)