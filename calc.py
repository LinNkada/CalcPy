#!/usr/bin/env python3
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Erro: Você deve digitar um número válido.")
        continue

    operation = input("Digite a operação (+, -, *, /): ")

    try:
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Você deve digitar um número válido.")
        continue

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue
    else:
        print("Erro: Operação inválida.")
        continue

    print(f"O resultado de {num1} {operation} {num2} = {result}")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        print("Saindo da calculadora.")
        break
