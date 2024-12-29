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


# Test for the provided expression
def test_for_each_with_non_empty_array():
    expression = """
    let array = [1, 2, 3]
    for (i in array) {
        print i
    }
    """
    output = execute_expression(expression)
    assert output == "1\n2\n3\n"


def test_for_each_with_empty_array():
    expression = """
    let empty_array = []
    for (i in empty_array) {
        print i
    }
    """
    output = execute_expression(expression)
    assert output == ""  # Empty array should produce no output