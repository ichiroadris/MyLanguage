import antlr4
from MyLangListener import MyLangListener

class Evaluator(MyLangListener):
    def __init__(self):
        self.environment = {}

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
              while(True):
                  print(5)


    # Entering an ifElseStatement
    def enterIfElseStatement(self, ctx):
        if self.evaluate_condition(ctx.condition()):
            print("Condition is true, executing if-block")
            for stmt in ctx.statement():
                self.process_statement(stmt)
        else:
            # Handle elif statements
            elif_blocks = ctx.ELIF()
            for i, elif_cond in enumerate(elif_blocks):
                if self.evaluate_condition(ctx.condition(i)):
                    print(f"Condition of elif {i + 1} is true, executing elif block")
                    for stmt in ctx.statement(i):
                        self.process_statement(stmt)
                    return
            # Handle else block if present
            if ctx.ELSE():
                print("Executing else block")
                for stmt in ctx.statement(len(elif_blocks)):
                    self.process_statement(stmt)

    # Processing each statement
    def process_statement(self, stmt):
        # You can expand this method to handle more types of statements as needed
        if stmt.variableDeclaration():
            self.enterVariableDeclaration(stmt.variableDeclaration())
        elif stmt.printStatement():
            self.enterPrintStatement(stmt.printStatement())
        elif stmt.whileStatement():
            self.enterWhileStatement(stmt.whileStatement())
        elif stmt.ifElseStatement():
            self.enterIfElseStatement(stmt.ifElseStatement())

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
            return expr_ctx.STRING().getText()[1:-1]  # Remove quotes
        elif expr_ctx.BOOLEAN():
            return expr_ctx.BOOLEAN().getText() == 'true'
        elif expr_ctx.array():
            return [self.evaluate_expression(e) for e in expr_ctx.array().expression()]
        elif expr_ctx.object():
            return {pair.STRING().getText()[1:-1]: self.evaluate_expression(pair.expression()) for pair in expr_ctx.object().pair()}
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
        if condition_ctx.expression():
            left = self.evaluate_expression(condition_ctx.expression(0))
            right = self.evaluate_expression(condition_ctx.expression(1))
            op = condition_ctx.COMPARISON_OP().getText()
            
            if op == ">":
                return left > right
            elif op == "<":
                return left < right
            elif op == "==":
                return left == right
            elif op == "!=":
                return left != right
            elif op == ">=":
                return left >= right
            elif op == "<=":
                return left <= right
        elif condition_ctx.BOOLEAN():
            return condition_ctx.BOOLEAN().getText() == 'true'
        
        return False

    def evaluate_condition(self, condition_ctx):
      # print(f"Evaluating condition: {condition_ctx}")
      
      if isinstance(condition_ctx, list):
          print(f"Condition is a list with {len(condition_ctx)} elements.")
          condition_ctx = condition_ctx[0]  # Extract the first (and only) element
      else:
        while(True):
          print(5)
          
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