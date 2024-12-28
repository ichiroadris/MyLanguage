grammar MyLang;

// Parser Rules
program      : statement+ ;
statement    : variableDeclaration
              | printStatement
              | whileLimitStatement
              | whileStatement
              | ifElseStatement
              | forStepStatement
              | forLoopStatement
              | passStatement
              | switchStatement;

variableDeclaration : LET ID '=' expression;
printStatement      : PRINT expression;
whileLimitStatement : WHILE '(' condition LIMIT INT')' '{' statement+ '}';
whileStatement : WHILE '(' condition ')' '{' statement* '}' ;
ifElseStatement
    : IF '(' condition ')' '{' statement* '}'
      ( ELIF '(' condition ')' '{' statement* '}' )*
      ( ELSE '{' statement* '}' )? ;
switchStatement
    : SWITCH '(' expression ')' '{'
        caseBlock*
        defaultBlock?
      '}' ;

caseBlock : CASE expression ':' statement+ ;
defaultBlock : DEFAULT ':' statement+ ;
passStatement : PASS ;

forStepStatement
    : FOR '(' start=INT 'to' goal=INT 'step' step=INT ')' '{' statement* '}';
forLoopStatement
    : FOR '(' INT ')' '{' statement* '}';

comment : '//' STRING* ;
multilineComment : '///' STRING* '///';
iterable            : array
                    | object
                    | ID ;
array               : '[' expression (',' expression)* ']' ;
object : '{' (pair (',' pair)*)? '}' ;
pair  : STRING ':' expression ;
condition           : expression COMPARISON_OP expression
                    | BOOLEAN ;
expression          : INT
                    | ID
                    | STRING
                    | array
                    | object
                    | '(' expression OPERATOR expression ')'
                    | expression '?' expression ':' expression ;

// Lexer Rules
// Keywords must come before ID
LIMIT   : 'limit';
WHILE   : 'while';
FOR     : 'for';
LET     : 'let';
ELIF    : 'else if';
PRINT   : 'print';
RETURN  : 'return';
IF      : 'if';
ELSE    : 'else';
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';
PASS    : 'pass';
TO      : 'to';
STEP    : 'step';

// Operators
OPERATOR: '+' | '-' | '*' | '/' | '%';
COMPARISON_OP: '>' | '<' | '==' | '!=' | '>=' | '<=';

// Literals
BOOLEAN : 'true' | 'false';
INT     : DIGIT+;
STRING  : '"' (~["\r\n\\] | '\\' .)* '"';

// Identifiers
ID      : LETTER (LETTER | DIGIT)*;

// Basic tokens
LETTER  : [a-zA-Z_];
DIGIT   : [0-9];

// Skip tokens
COMMENT : '//' ~[\r\n]* -> skip;
WS      : [ \t\r\n]+ -> skip;
NEWLINE : '\r'? '\n' -> skip;

