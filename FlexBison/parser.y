%{
#include <stdio.h>
#include <stdlib.h>
#include "parser.tab.h"
void yyerror(const char *s) { printf("ERRO: %s\n", s); }
%}

%token KEY PAREN AND OR IGUAL NOT LESS GREATER PRINT SCAN IF ELSE FOR SEMICOLON VAR IGUALIGUAL PLUS MINUS MULTIPLY DIV JOIN IDEN STR INT

%start program

%%

program       : statements
              ;

statements    : statement
              | statements statement
              ;

block         : KEY statements KEY
              ;

statement     : assignment
              | print_statement
              | if_statement
              | for_statement
              | var_statement
              ;

assignment    : IDEN IGUAL bool_expression
              ;

print_statement : PRINT PAREN bool_expression PAREN
              ;

if_statement  : IF bool_expression block
              | IF bool_expression block ELSE block
              ;

for_statement : FOR assignment SEMICOLON bool_expression SEMICOLON assignment block
              ;

var_statement : VAR IDEN type
              | VAR IDEN type IGUAL bool_expression
              ;

bool_expression : bool_term
              | bool_expression OR bool_term
              ;

bool_term     : rel_expression
              | bool_term AND rel_expression
              ;

rel_expression : expression IGUAL expression
              | expression GREATER expression
              | expression LESS expression
              ;

expression   : term
              | expression PLUS term
              | expression MINUS term
              | expression JOIN term
              ;

term         : factor
              | term MULTIPLY factor
              | term DIV factor
              ;

factor       : INT
              | STR
              | IDEN
              | PLUS factor
              | MINUS factor
              | NOT factor
              | PAREN bool_expression PAREN
              | SCAN
              ;

type         : INT
              | STR
              ;

%%
