%%
"charusat" { printf("university"); }
[^(\n)("charusat")]+  { printf("%s", yytext); }
\n         { printf("\n"); }
%%

int yywrap(void) {
    return 1;
}

int main(void) {
    yylex();
    return 0;
}
