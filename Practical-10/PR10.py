import re

token_pattern = r'(\d+\.\d+|\d+|[+\-*/^()])'
token_regex = re.compile(token_pattern)

def tokenize(expression):
    return [token for token in token_regex.findall(expression) if token.strip()]

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)
    elif operator == '^':
        values.append(left ** right)

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def evaluate_expression(expression):
    tokens = tokenize(expression)
    values = []
    operators = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.isdigit() or '.' in token:
            values.append(float(token))

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()

        elif token in '+-*/^':
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(token)):
                apply_operator(operators, values)
            operators.append(token)

        i += 1

    while operators:
        apply_operator(operators, values)

    return values[-1] if values else "Invalid expression"

expression = input("Enter an arithmetic expression: ")
result = evaluate_expression(expression)
print("Result:", result)