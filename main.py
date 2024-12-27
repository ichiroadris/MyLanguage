from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator_copy import Evaluator

# Input from the user
expression = """
let ab = 5
let bc = 10

if(1 > 5) {
  print ab
}

for(5) {
  print ab
}

for (1 to 8 step 2) {
  print loop
}

while (true limit 3) {
    print 3
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
