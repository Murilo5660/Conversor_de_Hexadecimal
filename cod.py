numero = int(input("Digite um número Decimal: "))
resultado = ""
num2 = numero
if numero == 0:
    resultado = "0"
else:
    while numero > 0:
        resto = numero % 16
        numero = numero // 16 
        if resto < 10:
            resultado = str(resto) + resultado
        elif resto == 10:
            resultado = "A" + resultado
        elif resto == 11:
            resultado = "B" + resultado
        elif resto == 12:
            resultado = "C" + resultado
        elif resto == 13:
            resultado = "D" + resultado
        elif resto == 14:
            resultado = "E" + resultado
        elif resto == 15:
            resultado = "F" + resultado
        else:
            resultado = ""

print(f"O número {num2} em Hexadecimal é: {resultado}")