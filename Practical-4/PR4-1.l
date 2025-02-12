%%

[0-9]+ {printf("%s\n",yytext);}

.

%%

int yywrap(void){
	return 1;
}

int main(void){
	yylex();
	return 0;
}