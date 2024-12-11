grammar MyLang;

program      : {statement NEWLINE} ;
statement    : variableDeclaration
              | printStatement
              | forEachStatement
              | forRangeStatement
              | whileLimitStatement
              | whileStatement
              | unlessStatement
              | ifElseStatement
              | passStatement
              | returnStatement ;
variableDeclaration : 'let' ID '=' expression;
printStatement      : 'print' expression;
forEachStatement    : 'for' '(' ID 'in' iterable ')' '{' {statement} '}' ;
forRangeStatement   : 'for' '(' ID 'from' INT 'to' INT ')' '{' {statement} '}';
forLoopStatement : 'for' '(' INT ')' '{' {statement} '}' ;
forStepStatement : 'for' ID 'from' INT 'to' INT 'step' INT '{' {statement} '}';
whileStatement : 'while' '(' condition ')' '{' {statement} '}' ;
whileLimitStatement : 'while' '(' condition ')' 'limit' '(' INT ')' '{' {statement} '}' ;
doWhileStatement : 'do' '{' {statement} '}' 'while' '(' condition ')' ;
unlessStatement     : 'unless' '(' condition ')' '{' {statement} '}';
returnStatement : 'return' expression ';' ;

ifElseStatement 
    : 'if' '(' condition ')' '{' (statement)* '}'
      ( 'else if' '(' condition ')' '{' (statement)* '}' )*
      ( 'else' '{' (statement)* '}' )? ;

switchStatement 
    : 'switch' '(' expression ')' '{' 
        ( 'case' literal (statement)+ )* 
        ( 'default' (statement)+ )? 
      '}' 'end switch' ;

passStatement       : 'pass' ;
comment : '//' STRING* ;
multilineComment : '///' STRING* '///';
iterable            : array
                    | object
                    | ID ;
array               : '[' {expression (',' expression)*} ']' ;
object              : '{' {STRING ':' expression (',' STRING ':' expression)*} '}' ;
condition           : expression comparisonOperator expression
                    | BOOLEAN ;
expression          : INT
                    | ID
                    | STRING
                    | array
                    | object
                    | functionCall
                    | '(' expression operator expression ')'
                    | expression '?' expression ':' expression ;
functionCall        : ID '(' {expression (',' expression)*} ')' ;
operator            : '+' 
                    | '-' 
                    | '*' 
                    | '/' 
                    | '%' ;
comparisonOperator  : '>' 
                    | '<' 
                    | '==' 
                    | '!=' 
                    | '>=' 
                    | '<=' ;
BOOLEAN             : 'true' | 'false' ;
INT       : digit+ ;
STRING    : '\'' ( ~[\'\\] | '\\' . )* '\'' ;

letter    : 'a' .. 'z' | 'A' .. 'Z' | '_';  
digit     : '0' .. '9'; 
ID        : letter (letter | digit)* ;  
literal : INT
        | STRING
        | BOOLEAN ;

