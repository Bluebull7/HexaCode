class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consume(self, expected_type):
        token = self.tokens[self.pos]
        if token[0] != expected_type:
            raise SyntaxError(f'Expected {expected_type}, got {token[0]}')
        self.pos += 1
        return token

    def parse(self):
        return self.program()

    def program(self):
        self.consume('KEYWORD')  # 'deb'
        body = []
        while self.tokens[self.pos][1] != 'fin':
            body.append(self.statement())
        self.consume('KEYWORD')  # 'fin'
        return body

    def statement(self):
        token = self.tokens[self.pos]
        if token[1] == 'impr':
            self.consume('KEYWORD')
            value = self.consume('NUMBER')
            return ('print', value[1])
        else:
            raise SyntaxError(f'Unknown statement: {token[1]}')
