distancia_percorrida = float(input("Digite a distância percorrida em Km"))

tarifa_base = 4.00
km_rodado = 0.25

valor_total =  tarifa_base + (km_rodado * distancia_percorrida)

print(f"Valor total da corrida: R${valor_total: .2f}")