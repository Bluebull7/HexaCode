class Evaluator:
    def __init__(self, ast):
        self.ast = ast

    def evaluate(self):
        for node in self.ast:
            self.execute(node)

    def execute(self, node):
        if node[0] == 'print':
            print(node[1])
