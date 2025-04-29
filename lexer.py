import re
from tokens import TokenType

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type.name}({self.value})"

def tokenize(code):
    token_specification = [
        # Literais
        ('FLOAT',     r'\d+\.\d+'),
        ('NUMBER',    r'\d+'),
        ('STRING',    r'"[^"\n]*"'),     # strings entre aspas duplas
        ('CHAR',      r"'[^'\n]'"),      # um caractere entre aspas simples
        ('BOOLEAN',   r'\btrue\b|\bfalse\b'),

        # Palavras-chave (priorizar antes de IDENT para evitar conflito)
        ('INT',       r'\bint\b'),
        ('FLOAT_KW',  r'\bfloat\b'),
        ('BOOLEAN_KW',r'\bboolean\b'),
        ('STRING_KW', r'\bstring\b'),
        ('CHAR_KW',   r'\bchar\b'),

        # Operadores e símbolos
        ('PLUS',      r'\+'),
        ('MINUS',     r'-'),
        ('TIMES',     r'\*'),
        ('DIVIDE',    r'/'),
        ('ASSIGN',    r'='),
        ('LPAREN',    r'\('),
        ('RPAREN',    r'\)'),
        ('SEMICOLON',      r';'),

        # Identificadores e ignorados
        ('IDENT',     r'[A-Za-z_]\w*'),
        ('SKIP',      r'[ \t\n]+'),
        ('MISMATCH',  r'.'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    get_token = re.compile(tok_regex).match
    line = code
    pos = 0
    tokens = []

    while pos < len(line):
        match = get_token(line, pos)
        if match is None:
            raise SyntaxError(f"Unexpected character: {line[pos]}")
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f"Unexpected token: {value}")
        else:
            token_type = TokenType[kind] if kind in TokenType.__members__ else TokenType.IDENT
            tokens.append(Token(token_type, value))
        pos = match.end()
    
    tokens.append(Token(TokenType.EOF, ''))
    return tokens