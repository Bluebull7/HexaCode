class Evaluator:
    def __init__(self, ast):
        self.ast = ast

    def evaluate(self, print_callback=None):
        """
        Evaluate the AST. If print_callback is provided, use it to handle printed output.
        """
        for node in self.ast:
            self.execute(node, print_callback)

    def execute(self, node, print_callback=None):
        if node[0] == 'print':
            output = node[1]
            if print_callback:
                print_callback(output)
            else:
                print(output)
