from enum import Enum

class TokenType(Enum):
    # Palavras-chave
    INT = "INT"
    FLOAT_KW = "FLOAT_KW"
    BOOLEAN_KW = "BOOLEAN_KW"
    STRING_KW = "STRING_KW"
    CHAR_KW = "CHAR_KW"

    # Literais
    NUMBER = "NUMBER"
    FLOAT = "FLOAT"
    STRING = "STRING"
    CHAR = "CHAR"
    BOOLEAN = "BOOLEAN"

    # Identificadores
    IDENT = "IDENT"

    # Operadores e símbolos
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDE = "/"
    ASSIGN = "="
    PLUS_ASSIGN = "+="
    MINUS_ASSIGN = "-="
    TIMES_ASSIGN = "*="
    DIVIDE_ASSIGN = "/="
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    NOT = "!"

    # Fim do arquivo
    EOF = "EOF"
