from lexer import tokenize
from parser import parse
from semantic import analyze
from codegen import generate_code

def main():
    with open("examples/example1.neo", "r") as f:
        source_code = f.read()

    tokens = tokenize(source_code)
    arv_sint = parse(tokens)
    typed_arv_sint = analyze(arv_sint)
    code = generate_code(typed_arv_sint)

    print(code)

if __name__ == "__main__":
    main()