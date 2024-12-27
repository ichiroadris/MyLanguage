import antlr4
from MyLangListener import MyLangListener

class Evaluator(MyLangListener):
    def __init__(self):
        self.environment = {}
        self.environment = {}
        self.should_execute = True  # Track if current block should execute

    # Entering a variableDeclaration
    def enterVariableDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        value = self.evaluate_expression(ctx.expression())
        self.environment[var_name] = value
        print(f"Declared variable {var_name} with value {value}")

    # Entering a printStatement
    def enterPrintStatement(self, ctx):
        value = self.evaluate_expression(ctx.expression())
        print(value)

    # Entering a whileStatement
    def enterWhileStatement(self, ctx):
      while self.evaluate_condition(ctx.condition()):
          print(f"Executing while block...")
          for stmt in ctx.statement():
              # self.process_statement(stmt)
              print(stmt.getText())


    # Entering an ifElseStatement
    def enterIfElseStatement(self, ctx):
        if self.evaluate_condition(ctx.condition(0)):
            statements = ctx.statement()  # Get all statements
            num_if_statements = len(statements[0].getText().split(';'))  # Count statements in if block
            for i in range(num_if_statements):
                self.process_statement(statements[i])
        elif ctx.ELIF():  # Elif conditions
            for i, elif_cond in enumerate(ctx.ELIF(), start=1):
                if self.evaluate_condition(ctx.condition(i)):  # Elif condition check
                    print(f"Elif {i} condition is true")
                    if hasattr(ctx.statement(i), '__iter__'):
                        for stmt in ctx.statement(i):  # Elif-specific statements
                            self.process_statement(stmt)
                    else:
                        self.process_statement(ctx.statement(i))
                    return
        elif ctx.ELSE():  # Else block
            # elif_count = ctx.getChildCount()  # Number of elif blocks
            # if elif_count != 0:
            length = len(ctx.statement())  # Access the else block statements
            stmt = ctx.statement(length-1)
            self.process_statement(stmt)



    # Processing each statement
    def process_statement(self, stmt):
        if stmt != None:
            # You can expand this method to handle more types of statements as needed
            if stmt.variableDeclaration():
                self.enterVariableDeclaration(stmt.variableDeclaration())
            elif stmt.printStatement():
                self.enterPrintStatement(stmt.printStatement())
            elif stmt.whileStatement():
                self.enterWhileStatement(stmt.whileStatement())
            elif stmt.ifElseStatement():
                self.enterIfElseStatement(stmt.ifElseStatement())
            elif stmt.whileStatement():
                self.enterWhileStatement(stmt.whileStatement())
            elif stmt.forEachStatement():
                self.enterForEachStatement(stmt.forEachStatement())
            elif stmt.forRangeStatement():
                self.enterForRangeStatement(stmt.forRangeStatement())
        else:
            print("Statement is null in process_statement(self, stmt)")

    # Evaluating an expression (simplified)
    def evaluate_expression(self, expr_ctx):
        if expr_ctx.INT():
            return int(expr_ctx.INT().getText())
        elif expr_ctx.ID():
            var_name = expr_ctx.ID().getText()
            if var_name in self.environment:
                return self.environment[var_name]
            else:
                print(f"Warning: Variable {var_name} not defined.")
                return 0
        elif expr_ctx.STRING():
            raw_string = expr_ctx.STRING().getText()  # Get the raw text, including quotes
            return raw_string[1:-1]  # Remove the first and last characters (quotes)
        elif expr_ctx.BOOLEAN():
            return expr_ctx.BOOLEAN().getText() == 'true'
        elif expr_ctx.array():
            return [self.evaluate_expression(e) for e in expr_ctx.array().expression()]
        elif expr_ctx.OPERATOR():
            left = self.evaluate_expression(expr_ctx.expression(0))
            right = self.evaluate_expression(expr_ctx.expression(1))
            op = expr_ctx.OPERATOR().getText()
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            elif op == "/":
                return left / right
            elif op == "%":
                return left % right
        return 0

    def evaluate_condition(self, condition_ctx):
        if isinstance(condition_ctx, list):
            condition_ctx = condition_ctx[0]
            
        if condition_ctx.COMPARISON_OP():
            left = self.evaluate_expression(condition_ctx.expression(0))
            right = self.evaluate_expression(condition_ctx.expression(1))
            op = condition_ctx.COMPARISON_OP().getText()
            
            operators = {
                ">": lambda x, y: x > y,
                "<": lambda x, y: x < y,
                "==": lambda x, y: x == y,
                "!=": lambda x, y: x != y,
                ">=": lambda x, y: x >= y,
                "<=": lambda x, y: x <= y
            }
            return operators[op](left, right)
            
        return condition_ctx.BOOLEAN().getText() == 'true'

          
      # Inspect the children of the condition
    #   print(f"Children of the condition: {condition_ctx.children}")

      
    # Continue with the evaluation...


    # Handle switch statement
    def enterSwitchStatement(self, ctx):
        switch_expr = self.evaluate_expression(ctx.expression())
        print(f"Evaluating switch expression: {switch_expr}")
        for case in ctx.CASE():
            case_value = self.evaluate_expression(case.LITERAL())
            print(f"Evaluating case: {case_value}")
            if switch_expr == case_value:
                for stmt in case.statement():
                    self.process_statement(stmt)
        if ctx.DEFAULT():
            print("Executing default case.")
            for stmt in ctx.DEFAULT().statement():
                self.process_statement(stmt)

    def enterForEachStatement(self, ctx):
        loop_var = ctx.ID().getText()
        iterable = self.evaluate_expression(ctx.iterable())
        
        for item in iterable:
            # Create a new scope for the loop variable
            self.environment[loop_var] = item
            
            # Execute the loop body
            for stmt in ctx.statement():
                self.process_statement(stmt)
            
        # Remove the loop variable after the loop ends
        if loop_var in self.environment:
            del self.environment[loop_var]

    def enterForRangeStatement(self, ctx):
        # Extract the loop variable name
        loop_var = ctx.ID().getText()

        # Evaluate the start and end values (from and to)
        start = int(ctx.INT(0).getText())
        end = int(ctx.INT(1).getText())

        # Iterate over the range
        for value in range(start, end + 1):  # Assuming inclusive range
            # Assign the loop variable in the environment
            self.environment[loop_var] = value

            # Execute the loop body
            for stmt in ctx.statement():
                self.process_statement(stmt)

        # Remove the loop variable from the environment after the loop ends
        if loop_var in self.environment:
            del self.environment[loop_var]