from enum import Enum

class TokenType(Enum):
    # Palavras-chave
    INT = "INT"
    FLOAT_KW = "FLOAT_KW"
    BOOLEAN_KW = "BOOLEAN_KW"
    STRING_KW = "STRING_KW"
    CHAR_KW = "CHAR_KW"
    LER = "LER"
    ESCREVA = "ESCREVA"

    # Básicos
    NUMBER = "NUMBER"
    FLOAT = "FLOAT"
    STRING = "STRING"
    CHAR = "CHAR"
    BOOLEAN = "BOOLEAN"

    # Identificadores
    IDENT = "IDENT"

    # Operadores Aritméticos
    PLUS = "+"
    MINUS = "-"
    TIMES = "*"
    DIVIDE = "/"
    EXPONENTIATION = "**"

    # Operadores Compostos
    PLUS_ASSIGN = "+="
    MINUS_ASSIGN = "-="
    TIMES_ASSIGN = "*="
    DIVIDE_ASSIGN = "/="

    # Operadores Unários / Lógicos
    NOT = "!"
    
    # Símbolos
    ASSIGN = "="
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"

    # Fim do arquivo
    EOF = "EOF"
