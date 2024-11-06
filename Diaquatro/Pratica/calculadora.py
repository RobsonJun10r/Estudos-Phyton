numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite o tipo da operação ( +, -, *, /)")

if operacao == "+":
    soma = numero1 + numero2
    print("Resultado: ", soma)
elif operacao == "-":
    sub = numero1 - numero2
    print("Resultado: ", sub)
elif operacao == "*":
    mult = numero1 * numero2
    print("Resultado: ", mult)
elif operacao == "/":
   if numero2 != 0:
       resultado = numero1 / numero2
       print("Resultado", resultado)
   else:
       print("Erro: Divisão por zero!")
else:
    print("Esta não é uma operação válida")