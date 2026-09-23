import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.linear_model import LogisticRegression


# 1. Cargar el dataset preparado
datos = np.load("dataset_preparado.npz")

X_train = datos["X_train"]
X_test = datos["X_test"]
y_train = datos["y_train"]
y_test = datos["y_test"]

print("Dataset cargado correctamente.")
print(f"Entrenamiento: {X_train.shape}")
print(f"Prueba: {X_test.shape}")
print(f"Clases: {np.unique(y_train)}")


# 2. Modelo base: Regresión Logística
modelo_base = LogisticRegression(random_state=42)

modelo_base.fit(X_train, y_train)

precision_base = modelo_base.score(X_test, y_test)

print("\nModelo base - Regresión Logística")
print(f"Precisión: {precision_base:.4f}")


# 3. Crear la red neuronal
modelo = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


# 4. Configurar el modelo
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# 5. Entrenar la red neuronal
historial = modelo.fit(
    X_train,
    y_train,
    epochs=40,
    batch_size=8,
    validation_split=0.20,
    verbose=1
)


# 6. Evaluar la red neuronal
perdida, precision = modelo.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nRed neuronal")
print(f"Pérdida: {perdida:.4f}")
print(f"Precisión: {precision:.4f}")


# 7. Graficar las curvas de entrenamiento
plt.figure(figsize=(10, 5))

plt.plot(
    historial.history["accuracy"],
    label="Precisión de entrenamiento"
)

plt.plot(
    historial.history["val_accuracy"],
    label="Precisión de validación"
)

plt.title("Entrenamiento del Clasificador de Lluvia")
plt.xlabel("Época")
plt.ylabel("Precisión")
plt.legend()
plt.grid(True)

plt.savefig(
    "curvas_entrenamiento_lluvia.png",
    dpi=300
)

plt.show()


# 8. Guardar el modelo
modelo.save("modelo_lluvia.keras")

print("\nModelo guardado correctamente.")
print("Archivo generado: modelo_lluvia.keras")