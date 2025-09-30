# Conversor de Decimal para Hexadecimal
# Autor: [Seu nome aqui]
# Data: 30/09/2025
# Professor: Fernando

# Solicita o número ao usuário
numero_decimal = int(input("Digite um número decimal: "))

# Verifica se o número é zero (caso especial)
if numero_decimal == 0:
    print("O número 0 em hexadecimal é: 0")
else:
    resultado_hex = ""  # Variável para armazenar o resultado final

    numero = numero_decimal  # Criamos uma cópia para fazer as divisões

    while numero > 0:
        resto = numero % 16  # Calcula o resto da divisão por 16

        # Converte o resto em hexadecimal
        if resto < 10:
            digito = str(resto)
        elif resto == 10:
            digito = "A"
        elif resto == 11:
            digito = "B"
        elif resto == 12:
            digito = "C"
        elif resto == 13:
            digito = "D"
        elif resto == 14:
            digito = "E"
        elif resto == 15:
            digito = "F"

        # Constrói o número hexadecimal (ordem invertida dos restos)
        resultado_hex = digito + resultado_hex

        # Atualiza o número com a divisão inteira por 16
        numero = numero // 16

    # Exibe o resultado
    print(f"O número {numero_decimal} em hexadecimal é: {resultado_hex}")
