%{
#include <stdio.h>
#include <stdlib.h>

#include "parser.tab.h"
%}

%%
[ \t\n]                     ; // Espaços em branco ignorados

"ಠ_ಠ"                       {return KEY;}
"ʕ•ᴥ•ʔ"                     {return PAREN;}
"🐱"                         {return AND;}
"🐶"                         {return OR;}
"IGUAL"                      {return IGUAL;}
"NOPE"                       {return NOT;}
"<:"                         {return LESS;}
">:"                         {return GREATER;}

"YELL"                       {return PRINT;}

"©"                          {return SCAN;}

"LOL"                        {return IF;}
"ROFL"                       {return ELSE;}

"EPICFAIL"                   {return FOR;}
"<3"                         {return SEMICOLON;}

"MAGIC"                      {return VAR;}

"IGUAL?"                     {return IGUALIGUAL;}
"\+OMG"                      {return PLUS;}
"-OMG"                       {return MINUS;}
"•"                          {return MULTIPLY;}
"÷"                          {return DIV;}
"."                          {return JOIN;}

[a-zA-Z][a-zA-Z0-9_]*         {return IDEN;}
[0-9]+                        {return INT;}
\"[^\"]*\"                   {return STR;}

.                             {printf("Unknown token!\n"); yyterminate();}
%%