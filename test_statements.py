from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator

def run_test(test_code, test_name):
    print(f"\nRunning test: {test_name}")
    print("Input code:")
    print(test_code)
    print("\nOutput:")

    input_stream = InputStream(test_code)
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()

    evaluator = Evaluator()
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)
    print("\n" + "="*50)

# Test 1: Simple pass statement
test_pass = """
let x = 10
if (x > 5) {
    pass
}
print "After pass"
"""
run_test(test_pass, "Simple pass statement")

# Test 2: Pass in multiple branches
test_pass_branches = """
let x = 0
if (x > 0) {
    pass
} else {
    print "x is not positive"
}

if (x == 0) {
    pass
} else {
    print "x is not zero"
}
"""
run_test(test_pass_branches, "Pass in multiple branches")

# Test 3: Basic switch statement
test_switch_basic = """
let value = 2
switch (value) {
    case 1: print "One"
    case 2: print "Two"
    default: print "Other"
}
"""
run_test(test_switch_basic, "Basic switch statement")

# Test 4: Switch with multiple statements in cases
test_switch_multiple = """
let value = 1
switch (value) {
    case 1:
        print "One"
        print "First case"
    case 2:
        print "Two"
        print "Second case"
    default:
        print "Other"
        print "Default case"
}
"""
run_test(test_switch_multiple, "Switch with multiple statements")

# Test 5: Switch with variables
test_switch_variables = """
let x = 5
let y = 5
switch (x) {
    case y: print "x equals y"
    case 10: print "x is 10"
    default: print "no match"
}
"""
run_test(test_switch_variables, "Switch with variables")

# Test 6: Switch with expressions
test_switch_expressions = """
let x = 10
switch ((x - 5)) {
    case 5: print "x - 5 equals 5"
    case 0: print "x - 5 equals 0"
    default: print "no match"
}
"""
run_test(test_switch_expressions, "Switch with expressions")