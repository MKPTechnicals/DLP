import re

temp_count = 1
quadruples = []

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

def generate_quadruple(operator, operand1, operand2, result):
    quadruples.append([operator, operand1, operand2, result])

def tokenize(expression):
    token_pattern = r'(\d+\.\d+|\d+|[+\-*/^()])'
    token_regex = re.compile(token_pattern)
    return [token for token in token_regex.findall(expression) if token.strip()]

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def parse_expression(tokens):
    global quadruples
    operands = []
    operators = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.isdigit() or '.' in token:
            operands.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                op = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                result = new_temp()
                generate_quadruple(op, operand1, operand2, result)
                operands.append(result)
            operators.pop() 
        elif token in "+-*/":
            while (operators and operators[-1] in "+-*/" and
                   precedence(operators[-1]) >= precedence(token)):
                op = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                result = new_temp()
                generate_quadruple(op, operand1, operand2, result)
                operands.append(result)
            operators.append(token)
        i += 1

    while operators:
        op = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        result = new_temp()
        generate_quadruple(op, operand1, operand2, result)
        operands.append(result)

    return operands[-1]

def evaluate(expression):
    tokens = tokenize(expression)
    parse_expression(tokens)
    return quadruples

def print_quadruples(quadruples):
    print("Operator | Operand 1 | Operand 2 | Result")
    for quad in quadruples:
        print(f"{quad[0]:<8} | {quad[1]:<9} | {quad[2]:<9} | {quad[3]}")

expression = input("Enter an arithmetic expression: ")
quadruples = evaluate(expression)
print_quadruples(quadruples)
