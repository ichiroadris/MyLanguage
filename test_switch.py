from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator

def test_switch():
    # Test 1: Basic switch with matching case
    input_stream = InputStream("""
    let value = 1
    switch (value) {
        case 1
            print "One"
        case 2
            print "Two"
        default
            print "Other"
    } end switch
    """)

    # Test 2: Switch with default case
    input_stream2 = InputStream("""
    let value = 5
    switch (value) {
        case 1
            print "One"
        case 2
            print "Two"
        default
            print "Number not found"
    } end switch
    """)

    # Test 3: Switch with string values
    input_stream3 = InputStream("""
    let color = "red"
    switch (color) {
        case "red"
            print "Stop"
        case "green"
            print "Go"
        case "yellow"
            print "Caution"
        default
            print "Invalid color"
    } end switch
    """)

    # Test 4: Switch with multiple statements in cases
    input_stream4 = InputStream("""
    let num = 1
    switch (num) {
        case 1
            let result = "Starting"
            print result
            print "Processing case 1"
        case 2
            print "Case 2"
        default
            print "Default case"
    } end switch
    """)

    test_cases = [
        (input_stream, "Basic switch test"),
        (input_stream2, "Switch with default case test"),
        (input_stream3, "Switch with string values test"),
        (input_stream4, "Switch with multiple statements test")
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
    test_switch()