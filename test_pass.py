from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator

def test_pass():
    # Test 1: Simple pass statement
    input_stream = InputStream("""
    if (true) {
        pass
    }
    print "After pass"
    """)

    # Test 2: Pass in a while loop
    input_stream2 = InputStream("""
    let count = 0
    while (count < 3) {
        pass
        let count = count + 1
    }
    print "Loop completed"
    """)

    # Test 3: Pass with multiple statements
    input_stream3 = InputStream("""
    let x = 10
    if (x > 5) {
        pass
    } else {
        print "x is less than or equal to 5"
    }
    print "Test completed"
    """)

    test_cases = [
        (input_stream, "Simple pass test"),
        (input_stream2, "Pass in while loop test"),
        (input_stream3, "Pass in if-else test")
    ]

    for input_stream, test_name in test_cases:
        print(f"\nRunning {test_name}:")
        lexer = MyLangLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MyLangParser(stream)
        tree = parser.program()

        evaluator = Evaluator()
        walker = ParseTreeWalker()
        walker.walk(evaluator, tree)

if __name__ == '__main__':
    test_pass()