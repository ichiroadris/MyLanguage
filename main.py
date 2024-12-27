from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator

# Input from the user
expression = """
let a = (5+1)
print "ahmed is a good guy"

if(false) {
  print a
} else if(true) {
  print 100
} else {
  print (10 + 2)
}

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
