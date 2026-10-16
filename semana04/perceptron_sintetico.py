import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# 1. Crear datos sintéticos
X, y = make_classification(
    n_samples=500,
    n_features=4,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    random_state=42
)

# 2. Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 3. Estandarizar los datos
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Crear la red neuronal
modelo = tf.keras.Sequential([
    tf.keras.Input(shape=(4,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

# 5. Configurar el entrenamiento
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# 6. Entrenar la red neuronal
historial = modelo.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.20,
    verbose=1
)

# 7. Evaluar el modelo
perdida, precision = modelo.evaluate(X_test, y_test, verbose=0)

print("\nResultados del modelo:")
print(f"Pérdida: {perdida:.4f}")
print(f"Precisión: {precision:.4f}")

# 8. Mostrar las curvas de entrenamiento
plt.figure(figsize=(10, 5))

plt.plot(historial.history["accuracy"], label="Precisión de entrenamiento")
plt.plot(
    historial.history["val_accuracy"],
    label="Precisión de validación"
)

plt.title("Entrenamiento del Perceptrón Sintético")
plt.xlabel("Época")
plt.ylabel("Precisión")
plt.legend()
plt.grid(True)

plt.savefig("curvas_entrenamiento_sintetico.png", dpi=300)
plt.show()