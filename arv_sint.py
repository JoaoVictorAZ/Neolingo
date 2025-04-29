class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name

class Declaration(ASTNode):
    def __init__(self, var_type, name):
        self.var_type = var_type
        self.name = name

class Assignment(ASTNode):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr