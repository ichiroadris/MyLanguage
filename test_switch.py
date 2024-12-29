import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys


# Helper function to execute the code and capture output
def execute_expression(expression: str) -> str:
    input_stream = InputStream(expression)

    # Lexical and syntactical analysis
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()  # Assuming 'program' is the start rule in your grammar

    # Listener-based evaluation
    calc_evaluator = Evaluator()

    # Capture the output printed by the evaluator
    captured_output = StringIO()
    sys.stdout = captured_output  # Redirect stdout to capture print statements

    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    sys.stdout = sys.__stdout__  # Reset redirect.

    return captured_output.getvalue()


def test_basic_switch():
    expression = """
    let value = 1
    switch (value) {
        case 1
            print "One"
            break
        case 2
            print "Two"
            break
        default
            print "Other"
    } end switch
    """
    output = execute_expression(expression)
    assert output.strip() == "One"


# def test_switch_with_default():
#     expression = """
#     let value = 5
#     switch (value) {
#         case 1
#             print "One"
#             break
#         case 2
#             print "Two"
#             break
#         default
#             print "Number not found"
#     } end switch
#     """
#     output = execute_expression(expression)
#     assert output.strip() == "Number not found"


def test_switch_with_strings():
    expression = """
    let color = "red"
    switch (color) {
        case "red"
            print "Stop"
            break
        case "green"
            print "Go"
            break
        case "yellow"
            print "Caution"
            break
        default
            print "Invalid color"
    } end switch
    """
    output = execute_expression(expression)
    assert output.strip() == "Stop"


def test_switch_multiple_statements():
    expression = """
    let num = 1
    switch (num) {
        case 1
            let result = "Starting"
            print result
            print "Processing case 1"
            break
        case 2
            print "Case 2"
            break
        default
            print "Default case"
    } end switch
    """
    output = execute_expression(expression)
    assert output.strip() == "Starting\nProcessing case 1"


# def test_switch_fallthrough():
#     expression = """
#     let value = 1
#     switch (value) {
#         case 1
#             print "One"
#             // Intentional fallthrough
#         case 2
#             print "Two"
#             break
#         default
#             print "Other"
#     } end switch
#     """
#     output = execute_expression(expression)
#     assert output.strip() == "One\nTwo"


def test_switch_empty_case():
    expression = """
    let value = 2
    switch (value) {
        case 1
            break
        case 2
            print "Two"
            break
        default
            print "Other"
    } end switch
    """
    output = execute_expression(expression)
    assert output.strip() == "Two"


def test_switch_expression():
    expression = """
    let x = 5
    let y = 3
    switch (x + y) {
        case 8
            print "Eight"
            break
        case 7
            print "Seven"
            break
        default
            print "Other sum"
    } end switch
    """
    output = execute_expression(expression)
    assert output.strip() == "Eight"


def test_switch_nested():
    expression = """
    let outer = 1
    switch (outer) {
        case 1
            let inner = 2
            switch (inner) {
                case 2
                    print "Nested match"
                    break
                default
                    print "Nested default"
            } end switch
            break
        default
            print "Outer default"
    } end switch
    """
    output = execute_expression(expression)
    assert output.strip() == "Nested match"
