# Troll Programming Language

### Introduction:
The "Troll" programming language was created with the primary goal of entertaining programmers and internet meme enthusiasts. It combines elements of humor and internet meme culture with programming concepts to create a unique experience.

### Key Features:

*Absurd Syntax*: The syntax used in the "Troll" language has intentionally been made absurd and unconventional. Of programming keywords it incorporates humorous words and terms.

*Meme Typing*: In "Troll" data types are expressed using internet memes, which adds an aspect, to the language known as meme typing.

*Humorous Comments*: A relaxed atmosphere is encouraged in "Troll" code through the use of comments filled with references to memes. It creates an environment where humor is embraced.

### Purpose:
It's important to note that the purpose of the "Troll" language is not meant to be taken 
It is designed to bring joy and amusement to programmers providing a one of a kind coding experience that combines the realm of memes, with the coding community.

### Important Note:
While it's fun to explore the concept of a "Troll" programming language, it's crucial to remember that it's not suitable for real software development. When it comes to real projects, it's important to use appropriate programming languages and maintain a serious and professional codebase.


# EBMF

### Grammar

```
# General grammatical elements and rules:
#
# * Strings with double quotes (") denote KEYWORDS
# * Upper case names (NAME) denote rule names
# * e1, e2
#   Match e1, then match e2
# * e1 | e2
#   Match e1 or e2
# * { e }
#   Match zero or more occurrences of e.
# * [ e ]
#   Match one or none occurrences of e.
# * ( e )
#   Match expression.
```

```
### The default operations will be replaced by:
"!"  = NOPE
"-"  = -OMG
"+"  = +OMG
"=" = IGUAL
"==" = IGUAL?
"!=" = NOPE?
"||" = 🐶
"&&" = 🐱
">" = >:
"<" = <:
"*" = •
"/" = ÷
```


### Rule
```
PROGRAM = { STATEMENT } ;
BLOCK = "ಠ_ಠ", { STATEMENT }, "ಠ_ಠ" ;
STATEMENT = ( λ | ASSIGN | PRINT | IF | FOR | VAR) ;
ASSIGN = IDENTIFIER, "IGUAL", BOOLEAN EXPRESSION ;
PRINT = "YELL", "ʕ•ᴥ•ʔ", BOOLEAN EXPRESSION, "ʕ•ᴥ•ʔ" ;
IF = "LOL", BOOLEAN EXPRESSION, BLOCK, { "ROFL", BLOCK } ;
FOR = "EPICFAIL", ASSIGN, "<3", BOOLEAN EXPRESSION, "<3", ASSIGN, BLOCK ;
VAR = "MAGIC", IDENTIFIER, ( "InTiGeR" | "StRiNg" ), ( λ | "IGUAL", BOOLEAN EXPRESSION ) ;
BOOLEAN EXPRESSION = BOOLEAN TERM, { "🐶" BOOLEAN TERM } ;
BOOLEAN TERM = RELATIONAL EXPRESSION, { "🐱", RELATIONAL EXPRESSION } ;
RELATIONAL EXPRESSION = EXPRESSION, { ("IGUAL?" | ">:" | "<:"), EXPRESSION } ;
EXPRESSION = TERM, { ("+OMG" | "-OMG" | "." ), TERM } ;
TERM = FACTOR, { ("•" | "÷"), FACTOR } ;
FACTOR = NUMBER | STRING | IDENTIFIER | (("+OMG" | "-OMG" | "NOPE"), FACTOR) | "ʕ•ᴥ•ʔ", BOOLEAN EXPRESSION, "ʕ•ᴥ•ʔ" | SCAN ;
SCAN = "©", "ʕ•ᴥ•ʔ", "ʕ•ᴥ•ʔ" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
STRING = ( " | ' ), { λ | LETTER | DIGIT }, ( " | ' ) ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```

# Reference
- [Python Grammar](https://docs.python.org/3/reference/grammar.html?highlight=grammar)
