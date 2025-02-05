# f = open(r"/workspaces/DLP/Practical-3/test1.c", "r")

# f1 = f.readlines()

# keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "inline", "int", "long", "register", "restrict", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]
# operators = ["+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", "? :", "&", "*", "sizeof"]
# punctuations = ["(", ")", "{", "}", "[", "]", ";", ",", ".", ":", "->", "#", "##", "?"]

# print(f1)

# Update code to implement simple c lexical analyzer using python.

# Practical Definition
# Implementation of a Lexical Analyzer for C Language Compiler
# Objective
# To design and implement a lexical analyser, the first phase of a compiler, for the C programming language. The lexical analyser should perform the following tasks: (1) tokenizing the input string (2) removing comments (3) removing white spaces (4) entering identifiers into the symbol table (5) generating lexical errors.
# Language Constraint
# The program can be implemented in any programming language
# Input requirement
# •
# Accept a C source code file.
# •
# The input can contain keywords, identifiers, constants, strings, punctuation, operators, comments, and white spaces.
# Expected output
# •
# Tokenized output categorizing tokens into six types: keyword, identifier, constant, string, punctuation, and operator.
# •
# Symbol table with all identified identifiers stored.
# •
# Detection and reporting of lexical errors
# •
# Modified source code

# for 10th student and dont write any comments to explain

# for following:

# 1.
# int main() { 
# int a = 5 , 7H; 
# // assign value 
# char b = 'x';
# /* return 
# value */
# return a + b; 
# }

# 2.
# /* salary calculation*/
# void main() 
# { 
# long int bs, da, hra, gs; 
# //take basic salary as input 
# scanf("%ld",&bs); 
# //calculate allowances 
# da-bs*.40; 
# hra-bs*.20; 
# gs-bs+da+hra; 
# // display salary slip 
# printf("\n\nbs: %ld",bs); 
# printf("\nda %ld",da); 
# printf("\nhra: %ld",hra); 
# printf("\ngs: %ld",gs); 
# }

# 3.
# //user defined data type 
# struct student
# {
# int id; 
# float cgpa;
# }
# void main() 
# {
# student s;
# s.id=10; 
# s.cgpa=8.7;
# }

# 4.
# //function prototype 
# void add (int, int); 
# void main() 
# { 
# int a, b; 
# a=10; 
# b=20; 
# // function call 
# add (a, b);
# } 
# void add (int x, int y) 
# {
# return x + y;
# }

# expected output for testcase 1:
# TOKENS 
# Keyword: int 
# Identifier: main 
# Punctuation: ( 
# Punctuation:) 
# Punctuation: { 
# Keyword: int 
# Identifier: a 
# Operator: = 
# Constant: 5 
# Punctuation:. 
# Punctuation:: 
# Keyword: char 
# Identifier: b 
# Operator: = 
# String: 'x' 
# Punctuation:: 
# Keyword: return 
# Identifier: a 
# Operator: + 
# Identifier: b 
# Punctuation:: 
# Punctuation:}

# LEXICAL ERRORS 
# 7H invalid lexeme 
# SYMBOL TABLE 
# ENTRIES 
# 1) a 
# 2) b