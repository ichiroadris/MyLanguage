from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator

# Input from the user
expression = """
let c = 0

let x = 5
if (x > 10) {
    print "greater than 10"
} else if (x > 5) {
    print "greater than 5"
} else {
    print "5 or less"
}
    
if(false) {
  print 100
} else if(true) {
  print 99
} else {
  print "I am dumb : : )"
}

while(c < 1) {
  let c = (c+1)
  print "I am while loop"
  print c
}

print "ahmed"
"""

input_stream = InputStream(expression)

# Lexical and syntactical analysis
lexer = MyLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MyLangParser(token_stream)
tree = parser.program() # Assuming 'expr' is the start rule in your grammar

# Listener-based evaluation
calc_evaluator = Evaluator()
walker = ParseTreeWalker()
walker.walk(calc_evaluator, tree)

# Get the result from the evaluator
# result = calc_evaluator.(tree)
# print(f"Result: {result}")
