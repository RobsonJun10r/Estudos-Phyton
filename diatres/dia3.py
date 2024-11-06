a = 10
b = 5
soma = a + b

# Subtracao
diferenca = a - b

# Multiplicacao
produto = a * b

# Divisão
divisao = a / b

# Módulo
resto = a % b

# Exponenciação
potencia = a**b

# Divisão inteira
div_inteira = a//b

# Operadores de comparaçao = Permitem comparar valores e determinar relações entre eles, resultando em um valor booleano (True or False)

x = 10
y = 5

# Igual a
print(x == y) # False

# Diferente de
print(x != y) # True

# Maior que
print(x > y) # True

# Menor que
print(x < y) # False

# Maior ou igual a 
print(x >= 10) # True

# Menor ou igual a 
print(y <= 5) # True

# Operadores Lógicos = são usados para combinar múltiplas condições ou inverter o resultado de uma condição. Retornam Booleanos

idade = 21
possui_carteira = True

# Verificar se pode alugar carro
pode_alugar = (idade >= 21) and possui_carteira
print("Pode alugar carro? ", pode_alugar) # True

# Verifica se tem direito a meia entrada
estudante = False
idoso = idade >= 60
meia_entrada = (estudante or idoso)
print("Tem direito a meia entrada?", meia_entrada) # False

# Inverter condição
chovendo = False
nao_chovendo = not chovendo
print("Está chovendo?", chovendo) # False
print("Não está chovendo?", nao_chovendo) # True


# Exercicio padaria
pao = 3.50
leite = 4.20
cafe = 2.80

# Total da compra
total_da_compra = pao + leite + cafe

# Valor pago
valor_pago = 20

# Calcular troco
troco = valor_pago - total_da_compra

print("O total da sua conta foi: R$", total_da_compra)
print("Seu troco é: ", troco)


# Dados do estudante
nota_media = 8.5
frequencia = 98

aprovado = (nota_media >= 7 ) and (frequencia >= 75)
print("O aluno foi aprovado?", aprovado)