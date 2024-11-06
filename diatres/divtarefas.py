# Valor total da conta
conta = 150

# Amigos 
amigos = 3

#Valor por pessoa
valor_por_pessoa =  conta / amigos

# Verifica se a divisão é exata 
divisao_exata = (conta % amigos) == 0

print("Cada um deve pagar: R$", valor_por_pessoa)
print("A divisão é exata?", divisao_exata) # True
