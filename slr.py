class ProductionRule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
 
stack = '$'

n = int(input('Enter no. of production rules: '))
start_symbol = input('Enter start symbol: ')
print('Enter the productions in the form <NT> -> <RHS> :-')

#List to store all productions
productions = []

for i in range(n):
    prod_str_splitted = input().split('->')
    rule = ProductionRule(prod_str_splitted[0].strip(), prod_str_splitted[1].strip())
    productions.append(rule)

input_str = input('Enter the input string to parse: ')

str_index = 0

early_stop = False # Flag to do early stop for special grammars like the one mentioned at the top.

while True:
    if early_stop:
        break
    ch = ''
    if str_index < len(input_str):
        ch += input_str[str_index]
        str_index += 1

        stack += ch
        print('Stack: ', stack, end='\t')

        print('Buffer: ', input_str[str_index:], end='\t')
        print('SHIFT')

    j = 0
    while j<len(productions):
        try:
            stack_top = stack.index(productions[j].right)
            substr_length = len(productions[j].right)
        except ValueError:
            j += 1
            continue

        # Replacing matched part with LHS of production
        stack = stack[:stack_top] + productions[j].left + stack[stack_top + substr_length :]
        print('Stack: ', stack, end='\t')

        print('Buffer: ', input_str[str_index:], end='\t')
        print('REDUCE ', productions[j].left + ' -> ' + productions[j].right)

        if stack[1:]==start_symbol and str_index==len(input_str):
            early_stop = True
            print('String accepted')
            break
        # Restarting loop to check immediate reduction of newly derived production
        j = 0

    # Accept case
    # Stack - Start symbol, Buffer - Empty
    if stack[1:]==start_symbol and str_index==len(input_str):   
        print('String accepted')
        break

    if str_index==len(input_str):
        print('String not accepted')
        break
