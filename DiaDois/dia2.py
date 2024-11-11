idade =  21
nome = 'Robson'
altura = 1.80
estudante = True

# Números inteiros = são números sem casas decimais, positivos ou negativos incluindo zero

idade1 = 30
quantidade = -5
ano = 2021

# Números com ponto flutuante(Float) = São npumeros com casas decimais, também conhecidos como números reais.

altura1 = 1.75
peso = 68.5
temperatura = -3.4

# Cadeia de caracteres(String) = São sequências de caracteres(letras, números, símbolos) São representadas por '' ou ""

name = "João"
cidade = 'São Paulo'
mensagem = "Olá Mundo"

# Booleans = São valores lógicos que representam Verdadeiro(True) ou Falso(False)

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("Estudante:", estudante)

ano_nascimento = 2024 - idade
maior_de_idade = idade >= 18
print("Ano de Nascimento:", ano_nascimento)
print("É maior de idade?:", maior_de_idade)

frase = "Olá meu nome é" + nome + " e eu tenho " + str(idade) + " anos." #str(idade) converte numero para string
print(frase)

# Calculadora simples

numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))

soma = numero1 + numero2
subtracao = numero1 - numero2
mutiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('soma =', soma )
print('Subtração =', subtracao )
print('Multiplicação =', mutiplicacao )
print('Divisão =', divisao )

# Celsius para fahrenheit

celsius = float(input("Digite a temperatura em Celsius"))
fahrenheit = celsius * 9/5 + 32
print("A temperatura em fahrenheit é: ", fahrenheit)

# Área de um circulo

raio = float(input("Qual o raio do círculo?"))
pi = 3.14159
area = pi * raio**2
print("A área do círculo é:", area)