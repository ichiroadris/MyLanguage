import pytest
from antlr4 import *
from MyLangLexer import MyLangLexer
from MyLangParser import MyLangParser
from MyEvaluator import Evaluator
from io import StringIO
import sys


# Helper function to execute the expression and capture the output
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


# Test for the first for loop (i from 1 to 3)
def test_for_loop_ascending():
    expression = """
    for (i from 1 to 3) {
        print i
    }
    """
    output = execute_expression(expression)
    assert output == "1\n2\n3\n"  # Expected output


# Test for the second for loop (i from 3 to 1)
def test_for_loop_descending():
    expression = """
    for (i from 3 to 1) {
        print i
    }
    """
    output = execute_expression(expression)
    assert output == "3\n2\n1\n"  # Expected output


# Test for the third for loop (i from 1 to 1)
def test_for_loop_single_value():
    expression = """
    for (i from 1 to 1) {
        print i
    }
    """
    output = execute_expression(expression)
    assert output == "1\n"  # Expected output