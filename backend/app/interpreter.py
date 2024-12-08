from app.hexacode.lexer import Lexer
from app.hexacode.parser import Parser
from app.hexacode.evaluator import Evaluator

class HexaInterpreter:
    def __init__(self):
        self.lexer = Lexer()

    def tokenize(self, source_code):
        return self.lexer.lex(source_code)

    def execute(self, source_code, print_callback=None):
        """
        Parses and evaluates the source code.
        If a print_callback is provided, it is used for handling output.
        """
        # Tokenization
        tokens = self.tokenize(source_code)

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        # Evaluation
        evaluator = Evaluator(ast)
        return evaluator.evaluate(print_callback=print_callback)
 