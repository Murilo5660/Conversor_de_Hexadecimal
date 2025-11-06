# Conversor de Decimal para Hexadecimal

O programa recebe um número em **decimal** digitado pelo usuário e o converte para o formato **hexadecimal**, exibindo o resultado no final.

## Objetivo

Praticar **estruturas de repetição**, **divisão inteira**, **módulo (%)** e **manipulação de strings** em Python, simulando o funcionamento interno da conversão de base numérica.

## Passos realizados

1. Pedi ao usuário um número decimal com:

   ```python
   numero = int(input("Digite um número Decimal: "))
   ```
2. Armazenei o valor original em `num2` para exibir no final.
3. Usei um **loop `while`** para:

   * Dividir o número por 16.
   * Obter o **resto da divisão** (`resto = numero % 16`), que representa cada dígito hexadecimal.
   * Converter o resto em letras (A a F) quando o valor era entre 10 e 15.
   * Montar o resultado invertendo a ordem dos dígitos.
4. Exibi o resultado final formatado:

   ```python
   print(f"O número {num2} em Hexadecimal é: {resultado}")
   ```

## Explicação técnica

* **Base decimal (10)** → dígitos de 0 a 9.
* **Base hexadecimal (16)** → dígitos de 0 a 9 e letras A-F.
* O algoritmo divide sucessivamente o número por 16 até chegar a zero, guardando os restos.
* A conversão é feita “de trás para frente”, pois o primeiro resto corresponde ao último dígito hexadecimal.

## Exemplo de execução

```
Digite um número Decimal: 255  
O número 255 em Hexadecimal é: FF
```

## Dificuldades

1. Entender o raciocínio da **divisão sucessiva** e por que o resultado deve ser invertido.
2. Lembrar de converter os valores de 10 a 15 para **A, B, C, D, E, F**.
