# 📘 Assignment: Numerical Root Finding

## 🎯 Objective

Implemente e compare os métodos da bisseção e de Newton-Raphson para aproximar raízes de funções. Você investigará precisão, convergência e as condições em que cada método funciona.

## 📝 Tasks

### 🛠️ Implement the Bisection Method

#### Descrição
Complete `bisection()` no arquivo inicial. O método deve reduzir repetidamente um intervalo que contém uma raiz até encontrar uma aproximação com a precisão solicitada.

#### Requisitos
O programa concluído deve:

- Receber uma função, os limites `left` e `right`, uma tolerância e um número máximo de iterações.
- Retornar `(root, iterations)`, onde `root` é a aproximação encontrada e `iterations` é o número de passos realizados.
- Retornar um limite imediatamente quando a função já for zero nele.
- Exigir limites ordenados e uma mudança de sinal no intervalo; caso contrário, lançar `ValueError`.
- Parar quando `abs(function(root)) <= tolerance` e lançar `RuntimeError` se o limite de iterações for atingido primeiro.

### 🛠️ Implement Newton-Raphson

#### Descrição
Complete `newton_raphson()` usando a função e sua derivada para melhorar uma estimativa inicial. O processo deve parar quando o valor absoluto da função na aproximação for menor ou igual à tolerância.

#### Requisitos
O programa concluído deve:

- Receber a função, sua derivada, `initial_guess`, uma tolerância e um número máximo de iterações.
- Retornar `(root, iterations)` com a aproximação e o número de passos realizados.
- Lançar `ValueError` se a derivada for zero em uma iteração antes da convergência.
- Lançar `RuntimeError` se o método não atingir a tolerância dentro do limite de iterações.
- Aceitar uma estimativa inicial que já seja uma raiz, retornando zero iterações.

### 🛠️ Compare Convergence and Test Edge Cases

#### Descrição
Use os dois métodos para encontrar as raízes de `f(x) = x**2 - 2` e `g(x) = cos(x) - x`. Compare quantas iterações cada método precisa e explique o que acontece quando suas condições de uso não são satisfeitas.

#### Requisitos
O programa concluído deve:

- Encontrar `sqrt(2)` com bisseção no intervalo `[1, 2]` e com Newton-Raphson usando `1.5` como estimativa inicial.
- Encontrar a raiz de `cos(x) - x` com bisseção no intervalo `[0, 1]` e com Newton-Raphson usando `1.0` como estimativa inicial.
- Usar tolerância `1e-6` e confirmar que cada aproximação satisfaz `abs(function(root)) <= tolerance`.
- Comparar e registrar o número de iterações dos dois métodos para cada função.
- Testar um intervalo sem mudança de sinal e um caso em que a derivada seja zero; explicar por que cada caso falha.
- Resumir quando a bisseção é confiável e por que Newton-Raphson pode convergir mais rápido, mas depende da estimativa inicial.