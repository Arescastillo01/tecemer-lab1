import math


def sigmoide(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return math.tanh(x)


def relu(x):
    return max(0, x)


def leaky_relu(x):
    if x >= 0:
        return x
    else:
        return 0.01 * x


def softmax(valores):
    exponenciales = [math.exp(x) for x in valores]
    suma = sum(exponenciales)

    return [valor / suma for valor in exponenciales]


print("FUNCIONES DE ACTIVACIÓN")
print("-" * 90)

for x in range(-5, 6):
    print(
        f"x = {x:2} | "
        f"Sigmoide = {sigmoide(x):.3f} | "
        f"Tanh = {tanh(x):.3f} | "
        f"ReLU = {relu(x):.3f} | "
        f"Leaky ReLU = {leaky_relu(x):.3f}"
    )


print()
print("SOFTMAX")
print("-" * 30)

valores = [2, 1, 0]

resultado = softmax(valores)

for i in range(len(valores)):
    print(f"Valor {valores[i]} -> Probabilidad: {resultado[i]:.3f}")

print(f"Suma de probabilidades: {sum(resultado):.3f}")
