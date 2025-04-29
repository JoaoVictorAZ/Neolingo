from arv_sint import *
from tokens import TokenType

class SemanticError(Exception):
    pass

class Symbol:
    def __init__(self, name, type_):
        self.name = name
        self.type = type_

class SymbolTable:
    def __init__(self):
        self.table = {}

    def declare(self, name, type_):
        if name in self.table:
            raise SemanticError(f"Redeclaração da variável '{name}'")
        self.table[name] = Symbol(name, type_)

    def lookup(self, name):
        if name not in self.table:
            raise SemanticError(f"Variável '{name}' não declarada")
        return self.table[name]

def analyze_expression(expr, symtable):
    if isinstance(expr, Number):
        expr.type = 'int' if isinstance(expr.value, int) else 'float'
        return expr.type

    elif isinstance(expr, Variable):
        symbol = symtable.lookup(expr.name)
        expr.type = symbol.type
        return expr.type

    elif isinstance(expr, BinOp):
        left_type = analyze_expression(expr.left, symtable)
        right_type = analyze_expression(expr.right, symtable)

        if expr.op in (TokenType.PLUS, TokenType.MINUS, TokenType.TIMES, TokenType.DIVIDE):
            if left_type == right_type:
                expr.type = left_type
            elif 'float' in (left_type, right_type):
                expr.type = 'float'
            else:
                raise SemanticError(f"Incompatibilidade de tipos em operação {expr.op}")
            return expr.type
        else:
            raise SemanticError(f"Operador não suportado: {expr.op}")

    else:
        raise SemanticError("Expressão inválida")

def analyze(ast):
    symtable = SymbolTable()
    for stmt in ast:
        if isinstance(stmt, Declaration):
            symtable.declare(stmt.name, stmt.var_type.name.lower())

        elif isinstance(stmt, Assignment):
            symbol = symtable.lookup(stmt.name)
            expr_type = analyze_expression(stmt.expr, symtable)

            if symbol.type != expr_type:
                raise SemanticError(f"Tipos incompatíveis: {symbol.type} = {expr_type}")
            stmt.type = expr_type

        else:
            raise SemanticError(f"Comando não suportado: {stmt}")
    return ast
