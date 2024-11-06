valor_emprestimo = float(input("Qual valor do empréstimo?"))
renda_cliente = float(input("Qual sua renda mensal?"))
numero_parcelas = int(input("Em quantas parcelas gostaria de fazer?"))

valor_parcela = valor_emprestimo / numero_parcelas
limite_parcela = renda_cliente * 0.30

if (valor_parcela < limite_parcela):
    print(f"Parabéns seu empréstimo foi aprovado no valor de: {valor_emprestimo} em {numero_parcelas}X")
else:
    print("Seu empréstimo não foi aprovado")

