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
        print(ctx.condition())
        if self.evaluate_condition(ctx.condition()):
            print("Condition is true, executing if-block")
            for stmt in ctx.statement():
                self.process_statement(stmt)
        else:
            # Handle elif statements
            print("Condition is false, checking elif blocks")
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
                for stmt in ctx.statement():
                    self.process_statement(stmt)

     # Processing each statement
    def process_statement(self, stmt):
        if stmt.variableDeclaration():
            self.enterVariableDeclaration(stmt.variableDeclaration())
        elif stmt.printStatement():
            self.enterPrintStatement(stmt.printStatement())
        elif stmt.whileStatement():
            self.enterWhileStatement(stmt.whileStatement())
        elif stmt.ifElseStatement():
            self.enterIfElseStatement(stmt.ifElseStatement())
        elif stmt.forLoopStatement():
            self.enterForLoopStatement(stmt.forLoopStatement())
        elif stmt.forStepStatement():
            self.enterForStepStatement(stmt.forStepStatement())
        elif stmt.whileLimitStatement():
            self.enterWhileLimitStatement(stmt.whileStepStatement())

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
        print (condition_ctx)
        print(f"++++++++Evaluating condition: {condition_ctx[0].expression(0).getText()}++++++++")
        if condition_ctx[0].COMPARISON_OP():
            left = self.evaluate_expression(condition_ctx[0].expression(0))
            right = self.evaluate_expression(condition_ctx[0].expression(1))
            op = condition_ctx[0].COMPARISON_OP().getText()

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
                
    # Entering a forLoopStatement
    def enterForLoopStatement(self, ctx):
        print("Entering a for loop...")
        
        loop_count = ctx.INT()
        loop_count_INT = int(loop_count.getText()) - 1
        
        if not isinstance(loop_count_INT, int):
            print("Warning: parameter is not an integer.")
            return

        for i in range(loop_count_INT):
            for stmt in ctx.statement():
                self.process_statement(stmt)
                
     # Entering a forStepStatement
    def enterForStepStatement(self, ctx):
        print("Entering a for-step loop...")

        # Parse the start, goal, and step values from the context
        # Extract integers from the INT() tokens
        ints = [int(token.getText()) for token in ctx.INT()]
        if len(ints) != 3:
            print("Error: For-step loop requires exactly 3 integers (start, goal, step).")
            return

        start, goal, step = ints

        # Validate step to prevent infinite loops
        if step <= 0:
            print("Error: Step must be a positive integer.")
            return

        # Execute the loop
        current = start
        
        while current <= goal:
            self.environment["loop"] = current
            # Execute the statements inside the loop
            for stmt in ctx.statement():
                self.process_statement(stmt)
            
            # Increment the current value by the step
            current += step
            
        if "loop" in self.environment:
            del self.environment["loop"]

    def evaluate_condition2(self, condition_ctx):
        #print(condition_ctx)
        #print(f"++++++++Evaluating condition: {condition_ctx.getText()}++++++++")
        
        # Access the children of the condition context
        children = condition_ctx.children  # Assumes `condition_ctx` has child nodes for the condition
        
        if len(children) == 3:  # Typical binary condition like `1 < 2`
            lhs = int(children[0].getText())  # Left-hand side
            #print(lhs)
            op = children[1].getText()  # Operator (e.g., <, >, ==, etc.)
            rhs = int(children[2].getText())  # Right-hand side
            
            # Perform the comparison
            if op == ">":
                return lhs > rhs
            elif op == "<":
                return lhs < rhs
            elif op == "==":
                return lhs == rhs
            elif op == "!=":
                return lhs != rhs
            elif op == ">=":
                return lhs >= rhs
            elif op == "<=":
                return lhs <= rhs
        elif condition_ctx.BOOLEAN():  # For boolean values
            return condition_ctx.BOOLEAN().getText() == 'true' or 'True'
        
        return False  # Default return value for unsupported conditions


    
# Entering a whileLimitStatement
    def enterWhileLimitStatement(self, ctx):
        #print(ctx.condition().getText())
        limit_count = ctx.INT()
        limit = int(limit_count.getText()) - 1
        
        count = 0
        # Execute the while loop as long as the condition holds true and within the limit
        while self.evaluate_condition2(ctx.condition()) and count < limit:
            for stmt in ctx.statement():
                self.process_statement(stmt)
            count += 1  # Increment the loop count
