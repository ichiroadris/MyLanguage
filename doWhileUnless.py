from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from antlr4.tree.Tree import ParseTreeWalker

def main():
    # Test case for do-while loop
    expression = """
print "Testing do-while statement"
let x = 0
do {
    print x
    let x = (x + 1)
} while (x < 5)
"""

    input_stream = InputStream(expression)
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    tree = parser.program()

    evaluator = Evaluator()

    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)

    # Test case for unless statement
    expression2 = """
print "Testing unless statement"
let x = 10
unless (x > 20) {
    print "x is not greater than 20"
    let x = (x + 5)
    print x
}
"""
    input_stream2 = InputStream(expression2)
    lexer2 = MyLangLexer(input_stream2)
    token_stream2 = CommonTokenStream(lexer2)
    parser2 = MyLangParser(token_stream2)
    tree2 = parser2.program()

    evaluator2 = Evaluator()
    walker2 = ParseTreeWalker()
    walker2.walk(evaluator2, tree2)

if __name__ == "__main__":
    main()
