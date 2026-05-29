import re

TOKENS = [
    ('INICIO', r'inicio'),
    ('FIM', r'fim'),
    ('INTEIRO', r'inteiro'),
    ('MOSTRAR', r'mostrar'),

    ('NUMERO', r'\d+'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),

    ('SOMA', r'\+'),
    ('SUB', r'-'),
    ('MULT', r'\*'),
    ('DIV', r'/'),

    ('IGUAL', r'='),
    ('PONTO_VIRGULA', r';'),

    ('ABRE_PAR', r'\('),
    ('FECHA_PAR', r'\)'),

    ('ESPACO', r'[ \t\n]+'),
]

def lexer(codigo):
    tokens = []

    while codigo:
        match = None

        for tipo, regex in TOKENS:
            padrao = re.compile(regex)
            match = padrao.match(codigo)

            if match:
                texto = match.group(0)

                if tipo != 'ESPACO':
                    tokens.append((tipo, texto))

                codigo = codigo[len(texto):]
                break

        if not match:
            raise SyntaxError(f'Caractere inválido: {codigo[0]}')

    return tokens
