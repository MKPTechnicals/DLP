import re

def tokenize(expression):
    token_pattern = r'(\d+\.\d+|\d+|[a-zA-Z_]\w*|[+\-*/^()])'
    token_regex = re.compile(token_pattern)
    return [token for token in token_regex.findall(expression) if token.strip()]

def evaluate_constants(tokens):
    optimized_tokens = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        if token.isdigit() or '.' in token:
            optimized_tokens.append(token)
        elif token == '(':
            optimized_tokens.append(token)
        elif token == ')':
            optimized_tokens.append(token)
        elif token in '+-*/^':
            operand1 = optimized_tokens.pop() if optimized_tokens else None
            operand2 = tokens[i + 1] if i + 1 < len(tokens) else None

            if operand1 and operand2 and operand1.replace('.', '', 1).isdigit() and operand2.replace('.', '', 1).isdigit():
                if token == '+':
                    result = float(operand1) + float(operand2)
                elif token == '-':
                    result = float(operand1) - float(operand2)
                elif token == '*':
                    result = float(operand1) * float(operand2)
                elif token == '/':
                    result = float(operand1) / float(operand2)
                elif token == '^':
                    result = float(operand1) ** float(operand2)
                optimized_tokens.append(str(result))
                i += 1
            else:
                optimized_tokens.append(operand1)
                optimized_tokens.append(token)
        else:
            optimized_tokens.append(token)

        i += 1
    return optimized_tokens

def optimize_expression(expression):
    tokens = tokenize(expression)
    optimized_tokens = evaluate_constants(tokens)
    return ''.join(optimized_tokens)

expression = input("Enter an arithmetic expression: ")
optimized_expression = optimize_expression(expression)
print("Optimized Expression:", optimized_expression)
