import re

class Lexer:
    def __init__(self):
        self.TOKEN_SPECIFICATION = [
            ('KEYWORD', r'\b(deb|fin|impr|si|sin|tanq)\b'),  # Keywords
    ('NUMBER', r'\d+'),                              # Numbers
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),                # Variable names
    ('OP', r'[+\-*/=<>]'),                          # Operators
    ('NEWLINE', r'\n'),                             # Line endings
    ('SKIP', r'[ \t]+'),                            # Skip spaces and tabs
    ('MISMATCH', r'.'),                             # Any other character                 # Any other character
    ]

    def lex(self, source_code):
        tokens = []
        token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.TOKEN_SPECIFICATION)
        line_num = 1
        line_start = 0
        for mo in re.finditer(token_regex, source_code):
            kind = mo.lastgroup
            value = mo.group(kind)
            column = mo.start() - line_start
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'{value!r} unexpected on line {line_num}')
            else:
                tokens.append((kind, value, line_num, column))
         # Debugging: Print tokens
            print("Generated Tokens:", tokens)
        return tokens