peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura  **2)

peso_ideal = (imc >= 18.5) and (imc <= 24.9)

print("Seu imc é: ", imc)
print("Você está dentro do peso ideal?: ", peso_ideal)