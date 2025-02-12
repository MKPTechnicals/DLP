%{
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
%}

%%
[0-9]+ { printf("%s\n", yytext); }
[0-9]+ "**" [0-9]+ { 
    int base = atoi(yytext); 
    while (*yytext != '\0') yytext++; 
    yytext += 2; 
    int exponent = atoi(yytext); 
    int result = (int)pow(base, exponent); 
    printf("%d\n", result); 
}
[0-9]+ "*" [0-9]+ {
    int operand1 = atoi(yytext); 
    while (*yytext != '\0') yytext++; 
    yytext++; 
    int operand2 = atoi(yytext); 
    int result = operand1 * operand2; 
    printf("%d\n", result); 
}
. ;
%%

int yywrap(void) {
    return 1;
}

int main(void) {
    yylex();
    return 0;
}
