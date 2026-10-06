# INFORME: FUNCIONES DE ACTIVACIÓN

## 1. Introducción

Las funciones de activación son elementos fundamentales de las redes neuronales artificiales. Permiten que una red neuronal pueda aprender relaciones complejas a partir de los datos.

Una neurona recibe diferentes valores de entrada, realiza una operación matemática y posteriormente utiliza una función de activación para determinar qué valor debe transmitir a la siguiente capa.

Sin las funciones de activación, una red neuronal estaría limitada principalmente a realizar transformaciones lineales, lo que dificultaría representar problemas complejos.

En este informe se presentan algunas de las principales funciones de activación utilizadas en inteligencia artificial: **Sigmoide, Tanh, ReLU, Leaky ReLU y Softmax**.

---

## 2. ¿Qué es una función de activación?

Una función de activación es una función matemática que recibe como entrada el resultado de una operación realizada por una neurona y transforma ese resultado antes de enviarlo a la siguiente capa.

De forma simplificada:

**z = w₁x₁ + w₂x₂ + ... + b**

Después se aplica la función de activación:

**a = f(z)**

Donde:

- **x** = valores de entrada.
- **w** = pesos de la red neuronal.
- **b** = sesgo o bias.
- **z** = resultado de la combinación de entradas.
- **f(z)** = función de activación.
- **a** = salida de la neurona.

---

# 3. ¿Cuáles son las principales funciones de activación?

Las principales funciones que se estudian en este informe son:

1. **Sigmoide (Sigmoid)**
2. **Tangente hiperbólica (Tanh)**
3. **ReLU (Rectified Linear Unit)**
4. **Leaky ReLU**
5. **Softmax**

Cada una transforma las entradas de una manera diferente y tiene aplicaciones específicas.

---

# 4. Función Sigmoide

### ¿Qué hace?

La función Sigmoide transforma cualquier número de entrada en un valor comprendido entre **0 y 1**.

Su fórmula es:

**f(x) = 1 / (1 + e⁻ˣ)**

Por ejemplo:

- Si x es muy negativo, la salida se aproxima a 0.
- Si x = 0, la salida es 0.5.
- Si x es muy positivo, la salida se aproxima a 1.

Por esta característica, puede utilizarse para representar probabilidades, especialmente en problemas de clasificación binaria.

### Ejemplo

Si una neurona obtiene:

**x = 2**

la función Sigmoide produce aproximadamente:

**0.881**

---

# 5. Función Tanh

### ¿Qué hace?

La función Tanh, o tangente hiperbólica, transforma los valores de entrada en valores comprendidos entre **-1 y 1**.

Su fórmula es:

**f(x) = tanh(x)**

Por ejemplo:

- Si x es negativo, el resultado se aproxima a -1.
- Si x = 0, el resultado es 0.
- Si x es positivo, el resultado se aproxima a 1.

Una característica importante es que sus resultados están centrados alrededor de cero.

---

# 6. Función ReLU

### ¿Qué hace?

ReLU significa **Rectified Linear Unit** y es una de las funciones de activación más utilizadas en redes neuronales.

Su fórmula es:

**f(x) = max(0, x)**

Esto significa:

- Si x < 0 → salida = 0.
- Si x ≥ 0 → salida = x.

| Entrada | Salida ReLU |
|---:|---:|
| -5 | 0 |
| -2 | 0 |
| 0 | 0 |
| 2 | 2 |
| 5 | 5 |

ReLU es especialmente común en las capas ocultas de redes neuronales.

---

# 7. Función Leaky ReLU

### ¿Qué hace?

Leaky ReLU es una modificación de ReLU que permite conservar una pequeña parte de los valores negativos.

Una forma común es:

**f(x) = x, si x ≥ 0**

**f(x) = 0.01x, si x < 0**

Por ejemplo:

| Entrada | Salida |
|---:|---:|
| -5 | -0.05 |
| -2 | -0.02 |
| 0 | 0 |
| 2 | 2 |
| 5 | 5 |

La principal diferencia con ReLU es que los valores negativos no se convierten completamente en cero.

---

# 8. Función Softmax

### ¿Qué hace?

Softmax se utiliza principalmente en la capa de salida de redes neuronales para **clasificación multiclase**.

Convierte un conjunto de valores en probabilidades cuya suma es igual a 1.

Por ejemplo:

- Perro: 0.70
- Gato: 0.20
- Ave: 0.10

La suma es:

**0.70 + 0.20 + 0.10 = 1**

De esta manera, la red puede representar qué clase tiene mayor probabilidad.

# 9. Ejemplo de funcionamiento

Una parte de la salida será similar a:

```text
x = -5 | Sigmoide = 0.007 | Tanh = -1.000 | ReLU = 0.000 | Leaky ReLU = -0.050
x = -2 | Sigmoide = 0.119 | Tanh = -0.964 | ReLU = 0.000 | Leaky ReLU = -0.020
x =  0 | Sigmoide = 0.500 | Tanh = 0.000  | ReLU = 0.000 | Leaky ReLU = 0.000
x =  2 | Sigmoide = 0.881 | Tanh = 0.964  | ReLU = 2.000 | Leaky ReLU = 2.000
x =  5 | Sigmoide = 0.993 | Tanh = 1.000  | ReLU = 5.000 | Leaky ReLU = 5.000
```

Esto permite comprobar que una misma entrada puede producir resultados completamente diferentes dependiendo de la función utilizada.

---

# 10. Conclusiones

Las funciones de activación son fundamentales en las redes neuronales artificiales porque permiten introducir no linealidad en los modelos y posibilitan el aprendizaje de relaciones más complejas.

Sigmoide, Tanh, ReLU, Leaky ReLU y Softmax tienen comportamientos diferentes. Por esta razón, la elección de una función depende del tipo de red neuronal y del problema que se desea resolver.

El programa desarrollado en Python permite observar de manera práctica estas diferencias. Al introducir los mismos valores en las diferentes funciones, se puede comprobar cómo cada una transforma la información de entrada.

En conclusión, comprender las funciones de activación es importante para entender cómo una red neuronal procesa información y genera sus resultados.
