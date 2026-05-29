# MiniLang

Projeto desenvolvido para a AED de Compiladores.

## Objetivo

Criar uma mini linguagem contendo:

- análise léxica;
- análise sintática;
- gramática livre de contexto;
- validação de entradas.

## Linguagem

A linguagem possui:

- declaração de variáveis;
- operações matemáticas;
- comando mostrar.

## Tokens reconhecidos

- INICIO
- FIM
- INTEIRO
- MOSTRAR
- NUMERO
- ID
- SOMA
- SUB
- MULT
- DIV
- IGUAL
- PONTO_VIRGULA

## Exemplo válido

inicio

inteiro salario = 5000;

mostrar(salario);

fim

## Exemplo inválido

inicio

inteiro salario = ;

fim

## Estrutura do projeto

- lexer.py → analisador léxico
- parser.py → analisador sintático
- main.py → execução principal
- gramatica.txt → gramática da linguagem
