import antlr4
from MyLangListener import MyLangListener
from MyLangParser import MyLangParser
import MyGlobals as MyGlobals


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
        # print(f"Declared variable {var_name} with value {value}")

    # Entering a printStatement
    def enterPrintStatement(self, ctx):
        value = self.evaluate_expression(ctx.expression())
        if value is not None and value != 0:  # Only print if value is not None and not 0 (default for undefined)
            print(value)


    # Entering a whileStatement
    def enterWhileStatement(self, ctx):
        loop_count = 0
        max_iterations = 100
        MyGlobals.tree_walking_back = False  # Reset at start of while

        while loop_count < max_iterations:
            # Check condition first
            if not self.evaluate_condition(ctx.condition()):
                break

            self.environment['_loop_count'] = loop_count

            # Execute all statements in the while block
            block = ctx.block()  # Access the block
            if block:
                for stmt in block.statement():
                    self.process_statement(stmt)

            loop_count += 1

        if loop_count >= max_iterations:
            print("Warning: Maximum iteration limit reached")

        # Clean up and set flags
        if '_loop_count' in self.environment:
            del self.environment['_loop_count']
            MyGlobals.tree_walking_back = True  # Set walking back flag


    def enterIfElseStatement(self, ctx):
        # First check if the main 'if' condition is true
        if self.evaluate_condition(ctx.condition(0)):
            statements = ctx.block(0).statement()
            for statement in statements:
                self.process_statement(statement)
            return  # Exit after processing if block

        # If main 'if' was false, check all elif conditions
        elif_conditions_met = False
        if ctx.ELIF():
            for i, elif_cond in enumerate(ctx.ELIF(), start=1):
                if self.evaluate_condition(ctx.condition(i)):
                    elif_conditions_met = True
                    if hasattr(ctx.block(i).statement(), '__iter__'):
                        for stmt in ctx.block(i).statement():
                            self.process_statement(stmt)
                    else:
                        self.process_statement(ctx.block(i).statement())
                    break  # Exit after processing matching elif block

        # If no if/elif conditions were met, process else block if it exists
        if not elif_conditions_met and ctx.ELSE():
            last_block = ctx.block()[-1]  # Get the last block (else block)
            if hasattr(last_block.statement(), '__iter__'):
                for stmt in last_block.statement():
                    self.process_statement(stmt)
            else:
                self.process_statement(last_block.statement())



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
            elif stmt.forEachStatement():
                self.enterForEachStatement(stmt.forEachStatement())
            elif stmt.forRangeStatement():
                self.enterForRangeStatement(stmt.forRangeStatement())
            elif stmt.forLoopStatement():
                self.enterForLoopStatement(stmt.forLoopStatement())
            elif stmt.forStepStatement():
                self.enterForStepStatement(stmt.forStepStatement())
            elif stmt.whileLimitStatement():
                self.enterWhileLimitStatement(stmt.whileLimitStatement())
            elif stmt.unlessStatement():
                self.enterUnlessStatement(stmt.unlessStatement())
            elif stmt.doWhileStatement():
                self.enterDoWhileStatement(stmt.doWhileStatement())
            elif stmt.switchStatement():
                self.enterSwitchStatement(stmt.switchStatement())
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
                # Only print warning if not in a forEach loop
                if var_name != 'i':  # 'i' is commonly used in forEach loops
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

    # Handle a doWhileStatement
    def enterDoWhileStatement(self, ctx):
        first_run = True
        while True:  # runs at least once
            print(f"Executing do-while block...")
            for stmt in ctx.statement():
                self.process_statement(stmt)

            # Check the condition after executing the block
            if not first_run:
                if not self.evaluate_condition(ctx.condition()):
                    break  # Exit the loop if condition is False
            first_run = False

    # Handle unless statement
    def enterUnlessStatement(self, ctx):
        condition = self.evaluate_condition(ctx.condition())
        if not condition:  # Execute the block only if the condition is False
            print("Executing unless block...")
            for stmt in ctx.statement():
                self.process_statement(stmt)



    # Handle switch statement
    def enterSwitchStatement(self, ctx):
        # Evaluate the switch expression
        switch_value = self.evaluate_expression(ctx.expression())

        # Track if we've found a match and if we're in fallthrough mode
        found_match = False

        # Process each case
        for case_ctx in ctx.getChildren():
            # Skip non-case tokens
            if not isinstance(case_ctx, MyLangParser.SwitchStatementContext):
                continue

            # Get the case literal value
            if hasattr(case_ctx, 'LITERAL'):
                literal = case_ctx.LITERAL()
                if not literal:
                    continue

                literal_text = literal.getText()
                case_value = None

                # Parse the literal based on its type
                if literal_text.startswith('"'):
                    case_value = literal_text[1:-1]  # Remove quotes for strings
                elif literal_text in ['true', 'false']:
                    case_value = literal_text == 'true'
                else:
                    try:
                        case_value = int(literal_text)
                    except ValueError:
                        case_value = literal_text

                # Check for match or fallthrough
                if switch_value == case_value or found_match:
                    found_match = True

                    # Process all statements in this case
                    for stmt in case_ctx.statement():
                        if stmt.getText().strip() == 'break':
                            found_match = False
                            break
                        self.process_statement(stmt)

                    # If we hit a break, stop processing cases
                    if not found_match:
                        break

            # Handle default case
            elif hasattr(case_ctx, 'DEFAULT') and case_ctx.DEFAULT():
                if not found_match:
                    for stmt in case_ctx.statement():
                        if stmt.getText().strip() != 'break':
                            self.process_statement(stmt)

    def evaluate_literal(self, literal_ctx):
        if literal_ctx.INT():
            return int(literal_ctx.INT().getText())
        elif literal_ctx.STRING():
            # Remove the quotes from the string
            return literal_ctx.STRING().getText()[1:-1]
        elif literal_ctx.BOOLEAN():
            return literal_ctx.BOOLEAN().getText() == 'true'
        return None

    # Entering a forLoopStatement
    def enterForLoopStatement(self, ctx):
        print("Entering a for loop...")

        loop_count = ctx.INT()
        loop_count_INT = int(loop_count.getText()) - 1

        if not isinstance(loop_count_INT, int):
            print("Warning: parameter is not an integer.")
            return

        if loop_count_INT <= 0:
            print("Error: parameter must be a positive integer.")
            return

        for i in range(loop_count_INT):
            block = ctx.block()  # Access the block
            if block:
                for stmt in block.statement():
                    self.process_statement(stmt)

    def enterForStepStatement(self, ctx):

        # Parse the start, goal, and step values from the context
        # Extract integers from the INT() tokens
        ints = [int(token.getText()) for token in ctx.INT()]
        if len(ints) != 3:
            print("Error: For-step loop requires exactly 3 integers (start, goal, step).")
            return

        start, goal, step = ints

        if start > goal:
            step = step * -1
            goal = goal - 1
        else:
            goal = goal + 1
        # Iterate over the range
        for value in range(start, goal, step):  # Assuming inclusive range
            # Assign the loop variable in the environment
            self.environment["loop"] = value

            # Execute the loop body
            # Execute the loop body
            block = ctx.block()  # Access the block
            if block:
                for stmt in block.statement():
                    self.process_statement(stmt)
            # Remove the loop variable after the loop ends

        if "loop" in self.environment:
            del self.environment["loop"]

    def enterForEachStatement(self, ctx):
        loop_var = ctx.ID().getText()
        iterable = self.evaluate_expression(ctx.iterable())

        # Skip if iterable is empty
        if not iterable:
            return

        for item in iterable:
            # Create a new scope for the loop variable
            self.environment[loop_var] = item

            # Execute the loop body
            block = ctx.block()  # Access the block
            if block:
                for stmt in block.statement():
                    self.process_statement(stmt)

            # Remove the loop variable after each iteration
            if loop_var in self.environment:
                del self.environment[loop_var]

    def enterForRangeStatement(self, ctx):
        # Extract the loop variable name
        loop_var = ctx.ID().getText()

        # Evaluate the start and end values (from and to)
        start = int(ctx.INT(0).getText())
        end = int(ctx.INT(1).getText())
        step = 1 if start <= end else -1
        # Iterate over the range
        for value in range(start, end + step, step):  # Assuming inclusive range
            # Assign the loop variable in the environment
            self.environment[loop_var] = value

            # Execute the loop body
            # Execute the loop body
            block = ctx.block()  # Access the block
            if block:
                for stmt in block.statement():
                    self.process_statement(stmt)
            # Remove the loop variable after the loop ends
            if loop_var in self.environment:
                del self.environment[loop_var]

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
        limit = int(limit_count.getText())

        # Validate step to prevent infinite loops
        if limit <= 0:
            print("Error: Step must be a positive integer.")
            return

        count = 0
        # Execute the while loop as long as the condition holds true and within the limit
        while self.evaluate_condition2(ctx.condition()) and count < limit:
            block = ctx.block()  # Access the block
            if block:
                for stmt in block.statement():
                    self.process_statement(stmt)
            count += 1  # Increment the loop count
