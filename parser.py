from lexer import lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self, tipo):
        token = self.atual()

        if token and token[0] == tipo:
            self.pos += 1
        else:
            raise SyntaxError(f'Esperado {tipo}')

    def programa(self):
        self.consumir('INICIO')

        while self.atual() and self.atual()[0] != 'FIM':
            self.comando()

        self.consumir('FIM')

    def comando(self):
        token = self.atual()

        if token[0] == 'INTEIRO':
            self.declaracao()

        elif token[0] == 'MOSTRAR':
            self.mostrar()

        else:
            raise SyntaxError('Comando inválido')

    def declaracao(self):
        self.consumir('INTEIRO')
        self.consumir('ID')
        self.consumir('IGUAL')
        self.expressao()
        self.consumir('PONTO_VIRGULA')

    def mostrar(self):
        self.consumir('MOSTRAR')
        self.consumir('ABRE_PAR')
        self.expressao()
        self.consumir('FECHA_PAR')
        self.consumir('PONTO_VIRGULA')

    def expressao(self):
        self.termo()

        while self.atual() and self.atual()[0] in ['SOMA', 'SUB']:
            self.pos += 1
            self.termo()

    def termo(self):
        self.fator()

        while self.atual() and self.atual()[0] in ['MULT', 'DIV']:
            self.pos += 1
            self.fator()

    def fator(self):
        token = self.atual()

        if token[0] == 'NUMERO':
            self.consumir('NUMERO')

        elif token[0] == 'ID':
            self.consumir('ID')

        else:
            raise SyntaxError('Expressão inválida')
