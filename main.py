from lexer import lexer
from parser import Parser

with open('exemplos_validos.txt', 'r') as arquivo:
    codigo = arquivo.read()

tokens = lexer(codigo)

print('TOKENS:')
for token in tokens:
    print(token)

parser = Parser(tokens)

try:
    parser.programa()
    print('\nPrograma válido!')
except SyntaxError as erro:
    print('\nErro sintático:', erro)
