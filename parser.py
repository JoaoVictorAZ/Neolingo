from tokens import TokenType
from arv_sint import BinOp, Number, Variable, Declaration, Assignment

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, token_type):
        if self.current().type == token_type:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {token_type}, got {self.current().type}")

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        statements = []
        while self.current().type != TokenType.EOF:
            stmt = self.parse_statement()
            statements.append(stmt)
        return statements

    def parse_statement(self):
        tok = self.current()

        if tok.type in {
            TokenType.INT, TokenType.FLOAT_KW,
            TokenType.BOOLEAN_KW, TokenType.STRING_KW,
            TokenType.CHAR_KW
        }:
            return self.parse_declaration()
        elif tok.type == TokenType.IDENT:
            return self.parse_assignment()
        else:
            raise SyntaxError(f"Unexpected start of statement: {tok}")

    def parse_declaration(self):
        var_type = self.current().type
        self.eat(var_type)
        name_token = self.current()
        self.eat(TokenType.IDENT)
        self.eat(TokenType.SEMICOLON)
        return Declaration(var_type, name_token.value)

    def parse_assignment(self):
        name_token = self.current()
        self.eat(TokenType.IDENT)
        self.eat(TokenType.ASSIGN)
        expr = self.parse_expr()
        self.eat(TokenType.SEMICOLON)
        return Assignment(name_token.value, expr)

    def parse_expr(self):
        node = self.parse_term()
        while self.current().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current()
            self.eat(op.type)
            node = BinOp(node, op.type, self.parse_term())
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current().type in (TokenType.TIMES, TokenType.DIVIDE):
            op = self.current()
            self.eat(op.type)
            node = BinOp(node, op.type, self.parse_factor())
        return node

    def parse_factor(self):
        tok = self.current()
        if tok.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Number(int(tok.value))
        elif tok.type == TokenType.FLOAT:
            self.eat(TokenType.FLOAT)
            return Number(float(tok.value))
        elif tok.type == TokenType.IDENT:
            self.eat(TokenType.IDENT)
            return Variable(tok.value)
        elif tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.parse_expr()
            self.eat(TokenType.RPAREN)
            return node
        else:
            raise SyntaxError(f"Unexpected token: {tok}")

# Entry point
def parse(tokens):
    parser = Parser(tokens)
    return parser.parse()
