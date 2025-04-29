from arv_sint import BinOp, Number, Variable, Declaration, Assignment

class CodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 1
        self.declarations = []
        self.used_temps = []

    def new_temp(self):
        name = f"T{self.temp_count}"
        self.temp_count += 1
        self.used_temps.append(name)
        return name

    def emit(self, line):
        self.code.append(line)

    def gen(self, node):
        if isinstance(node, Number):
            temp = self.new_temp()
            self.emit(f"{temp} = {node.value};")
            return temp
        elif isinstance(node, Variable):
            return node.name
        elif isinstance(node, BinOp):
            left = self.gen(node.left)
            right = self.gen(node.right)
            temp = self.new_temp()
            op = node.op.value
            self.emit(f"{temp} = {left} {op} {right};")
            return temp
        elif isinstance(node, Declaration):
            # Declarar a variável (simplificação para int)
            self.emit(f"int {node.name};")
        elif isinstance(node, Assignment):
            value = self.gen(node.expr)
            self.emit(f"{node.name} = {value};")
        else:
            raise NotImplementedError(f"Unknown arv_sint node: {node}")

    def generate(self, arv_sint):
        self.code = []
        self.temp_count = 1
        self.used_temps = []
    
        for stmt in arv_sint:
            self.gen(stmt)
    
        self.declarations = [f"int {temp};" for temp in self.used_temps]
        return "\n".join(self.declarations + [""] + self.code)


def generate_code(arv_sint):
    cg = CodeGenerator()
    return cg.generate(arv_sint)
