from hexacode.lexer import Lexer
from hexacode.parser import Parser
from hexacode.evaluator import Evaluator

class HexaInterpreter:
    def __init__(self):
        self.lexer = Lexer()

    def tokenize(self, source_code):
        """Tokenizes the source code and returns the tokens."""
        return self.lexer.lex(source_code)

    def execute(self, source_code):
        """Parses and evaluates the source code."""
        # Tokenization
        tokens = self.tokenize(source_code)

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        # Evaluation
        evaluator = Evaluator(ast)
        return evaluator.evaluate()
