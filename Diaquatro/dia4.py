# Sintaxe
# if condição
# Bloco de código a ser executado se a condição for verdadeira
# else:
# bloco de código se a condição for falsa


idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# 3 - Declaração elif = permite verificar múltiplas condições. Se a primeira for falsa ele verifica a próxima e assim por diante

# if condicao1:
#     #  bloco de código se condição 1 for verdadeira
# elif condicao2:
#     #  bloco de código se condição 2 for verdadeira
# elif condicao3:
#     #  bloco de código se condição 3 for verdadeira
# else:
#     #  bloco de código se condição 3 for verdadeira

#Exemplo
nota = 100

if nota >= 90:
    print('A sua nota é A.')
elif nota >= 80:
    print('Sua nota é B.')
elif nota >= 70:
    print('Sua nota é C.')
else:
    print('Você precisa melhorar')

# Prática

clima = "nublado"

if clima == "ensolarado":
    print("Vista uma camiseta e short.")
elif clima == "nublado":
    print("Leve uma jaqueta.")
elif clima == "chuvoso":
    print("Não esqueça do guarda chuva.")
else: 
    print("Verifica a previsão do tempo.")

# Pratica 2

semaforo = input("Qual a cor do semáforo? ")

if semaforo == "Vermelho":
    print("Pare o veículo!")
elif semaforo == "Amarelo":
    print("Se prepare para parar!")
elif semaforo == "Verde":
    print("Siga em frente!")
else:
    print("Sinal em manutenção, proceda com cautela")

# Prática 3

valor_da_compra = 1000

if valor_da_compra >= 1000:
    desconto = valor_da_compra * 0.10
    print("Você ganhou 10%. O valor da sua compra ficou", desconto )
elif valor_da_compra >= 500:
    desconto = valor_da_compra * 0.5
    print("Você ganhou 5%. O valor da sua compra ficou", desconto)
else:
    desconto = 0
    print("Não há desconto disponível. ")

valor_final = valor_da_compra - desconto 

print("Valor final da compra: R$ ", valor_final)

# Pratica 4

dia_da_semana = "Sábado"
chovendo = True
if (dia_da_semana == "Sábado" or dia_da_semana == "domingo") and not chovendo:
    print("Vamos ao parque")
else:
    print("Assistir um filme")