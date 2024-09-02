# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para determinar a categoria com base no IMC
def determinar_categoria(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Entrada do usuário
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Determinação da categoria
categoria = determinar_categoria(imc)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Categoria: {categoria}")
