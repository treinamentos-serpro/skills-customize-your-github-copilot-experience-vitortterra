# 📘 Assignment: A Simple Programming Language Parser in Python

## 🎯 Objective

Construa um parser recursivo-descendente para uma pequena linguagem de expressões aritméticas. Você praticará tokenização, precedência de operadores, árvores sintáticas e validação de sintaxe.

## 📝 Tasks

### 🛠️ Tokenizar Expressões

#### Descrição
Implemente um tokenizer que percorra uma expressão e transforme cada número e operador em um token. A linguagem aceita números inteiros, espaços, os operadores `+`, `-`, `*` e `/`, e parênteses.

#### Requisitos
O programa concluído deve:

- Retornar números como tokens `("NUMBER", valor)` e operadores como pares com seus tipos, por exemplo `("PLUS", "+")`.
- Ignorar espaços em branco entre os tokens.
- Informar a posição de qualquer caractere que não pertença à linguagem.
- Tokenizar `12 + 3` como `[("NUMBER", 12), ("PLUS", "+"), ("NUMBER", 3)]`.

### 🛠️ Construir a Árvore Sintática

#### Descrição
Implemente o parser usando a gramática abaixo. Ele deve retornar uma árvore sintática abstrata (AST) com tuplas: `("number", valor)` para números e `(operador, esquerda, direita)` para operações. Use `"add"`, `"subtract"`, `"multiply"` e `"divide"` como nomes dos operadores na AST.

```text
expression = term (("+" | "-") term)*
term       = factor (("*" | "/") factor)*
factor     = NUMBER | "(" expression ")"
```

#### Requisitos
O programa concluído deve:

- Implementar `parse_expression()`, `parse_term()` e `parse_factor()` seguindo a gramática.
- Respeitar a precedência: multiplicação e divisão devem ser agrupadas antes de adição e subtração.
- Aceitar parênteses para controlar o agrupamento.
- Produzir para `2 + 3 * 4` a AST `("add", ("number", 2), ("multiply", ("number", 3), ("number", 4)))`.

### 🛠️ Detectar Erros de Sintaxe

#### Descrição
Faça o parser rejeitar expressões incompletas ou malformadas e apresentar uma mensagem que ajude a localizar o problema. O parser deve consumir a expressão inteira, sem ignorar tokens extras no final.

#### Requisitos
O programa concluído deve:

- Informar quando um operador não é seguido por um número ou parêntese válido.
- Informar quando um parêntese de abertura não tem o fechamento correspondente.
- Rejeitar entradas vazias, operadores consecutivos e tokens extras.
- Testar pelo menos três expressões válidas e três inválidas, incluindo `2 + * 3` e `(4 + 1`.